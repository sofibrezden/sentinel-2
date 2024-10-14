import cv2

from algorithm import FeatureMatcher, measure_performance, draw_matches

image1 = cv2.imread("./processed_tci_images/img_1.jpg")
image2 = cv2.imread("./processed_tci_images/img_2.jpg")

matcher = FeatureMatcher(detector_type="sift", ratio_thresh=0.6)

print(f"{matcher.detector_type.upper()} Matcher Performance:")

num_matches_sift, sift_time = measure_performance(matcher, image1, image2)
print(f"{matcher.detector_type.upper()}: {num_matches_sift} matches found.")

keypoints1, descriptors1 = matcher.find_keypoints_and_descriptors(image1)
keypoints2, descriptors2 = matcher.find_keypoints_and_descriptors(image2)

good_matches = matcher.match(descriptors1, descriptors2)
draw_matches(image1, keypoints1, image2, keypoints2, good_matches)
