import cv2
import matplotlib.pyplot as plt
import time


# Timer decorator to measure execution time of function
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds.")
        return result, execution_time

    return wrapper


class FeatureMatcher:
    def __init__(self, detector_type="SIFT", ratio_thresh=0.6):
        self.ratio_thresh = ratio_thresh
        self.detector_type = detector_type.lower()

        if self.detector_type == "sift":
            self.detector = cv2.SIFT_create()
        elif self.detector_type == "akaze":
            self.detector = cv2.AKAZE_create()
        elif self.detector_type == "orb":
            self.detector = cv2.ORB_create()
        else:
            raise ValueError(f"Unsupported detector type: {detector_type}. Supported types: SIFT, AKAZE, ORB.")

    def find_keypoints_and_descriptors(self, image):
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = self.detector.detectAndCompute(grayscale, None)
        return keypoints, descriptors

    def match(self, descriptors1, descriptors2):
        # Select the norm type based on the detector
        if self.detector_type == "sift":
            norm_type = cv2.NORM_L2
        else:
            norm_type = cv2.NORM_HAMMING

        bf = cv2.BFMatcher(norm_type)

        if self.detector_type == "sift":
            # KNN matching for SIFT (L2 Norm)
            matches = bf.knnMatch(descriptors1, descriptors2, k=2)
            good_matches = [m for m, n in matches if m.distance < self.ratio_thresh * n.distance]
        else:
            # Simple matching for AKAZE and ORB (Hamming Norm)
            matches = bf.match(descriptors1, descriptors2)
            good_matches = sorted(matches, key=lambda x: x.distance)

        return good_matches


@time_it
def measure_performance(matcher, image1, image2):
    keypoints1, descriptors1 = matcher.find_keypoints_and_descriptors(image1)
    keypoints2, descriptors2 = matcher.find_keypoints_and_descriptors(image2)

    if descriptors1 is None or descriptors2 is None:
        raise ValueError("No descriptors found in one of the images.")

    good_matches = matcher.match(descriptors1, descriptors2)
    num_matches = len(good_matches)

    return num_matches


def draw_matches(image1, keypoints1, image2, keypoints2, good_matches):
    matched_image = cv2.drawMatches(
        image1, keypoints1, image2, keypoints2, good_matches, None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    # Convert BGR to RGB for matplotlib display
    matched_image_rgb = cv2.cvtColor(matched_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))
    plt.imshow(matched_image_rgb)
    plt.title(f'Matches between two images ({len(good_matches)} good matches)')
    plt.axis('off')
    plt.show()
