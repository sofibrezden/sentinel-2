# 🛰️Satellite Image Matching Project

This project focuses on developing an algorithm for matching satellite images, specifically using Sentinel-2 images,
with different feature detection and matching techniques. The aim of the project is to build a robust algorithm that can
accurately match satellite images using keypoint detection methods.The dataset is obtained from Kaggle’s "Deforestation
in Ukraine" Sentinel-2 image dataset.

## 📑Table of Contents

- [Project Overview](#project-overview)
- [Dataset Preparation](#Dataset-Preparation)
- [Algorithms](#Algorithms)
- [Installation](#installation)
- [Usage](#Usage)
- [Project Structure](#project-structure)


## 🌍Project Overview

This project aims to create an efficient **satellite image matching algorithm** that can find corresponding points
between images. By leveraging various keypoint detection and feature matching
algorithms such as SIFT, AKAZE, and ORB, the goal is to evaluate which algorithm is best suited for this task in terms
of speed, accuracy, and robustness across seasonal variations.

## 📂Dataset Preparation

The dataset was obtained from
the [Deforestation in Ukraine Sentinel-2 dataset](https://www.kaggle.com/datasets/isaienkov/deforestation-in-ukraine/data).
The dataset was processed to extract and
convert the **True Color Images (TCI)** to a more manageable format (resized, converted to grayscale). The preprocessing
steps are documented in the `dataset_processing.ipynb` notebook, where images are resized and normalized before being
saved for keypoint detection.

## 🧠Algorithms

Three different algorithms were used for matching the satellite images:

- **SIFT (Scale-Invariant Feature Transform):** SIFT is a well-known feature detection and description algorithm that
  excels in detecting keypoints and features that are invariant to scale, rotation, and even some degree of affine
  transformations. It works particularly well on satellite images where features may appear at different scales or
  orientations. SIFT is known for its high accuracy and robustness, making it ideal for tasks requiring precise
  matching. However, it is computationally intensive and slower compared to other methods, which can be a drawback when
  working with large datasets or in real-time applications.
- **AKAZE (Accelerated-KAZE):** AKAZE is designed to offer a balance between speed and accuracy. It uses non-linear
  scale spaces for feature detection, which enhances its ability to handle texture-rich images like satellite data.
  AKAZE provides a compromise between the high accuracy of SIFT and the real-time performance of ORB, making it a solid
  choice for satellite image matching where both speed and reliability are important. While it’s faster than SIFT, AKAZE
  may not be as precise in certain edge cases, particularly with significant changes in illumination or viewpoint.
- **ORB (Oriented FAST and Rotated BRIEF):** ORB is the most efficient algorithm among the three in terms of speed,
  designed to be fast enough for real-time applications while maintaining a reasonable level of accuracy. It combines
  the FAST keypoint detector with the BRIEF descriptor, incorporating orientation information to handle rotation. ORB is
  well-suited for large satellite datasets or applications requiring rapid processing, but it may sacrifice some
  accuracy compared to SIFT and AKAZE, particularly when dealing with fine-grained details or significant changes in
  scale or rotation.

## ⚙️Installation

To get started with this project, follow these steps:

Clone the repository:

```
git clone https://github.com/sofibrezden/sentinel-2-test-task.git
cd sentinel-2-test-task
```

Create and activate a virtual environment:

```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

## 🚀Usage

To test the image matching algorithms, you can use the provided `inference.py script`. Make sure the required images are
in the `processed_tci_images/` folder.
Example usage:

```
python inference.py --image1 ./processed_tci_images/img_1.jpg --image2 ./processed_tci_images/img_2.jpg --algorithm sift
```

This will run the SIFT algorithm to match keypoints between the two images and display the results. You can
replace `sift` with `akaze` or `orb` to test the other algorithms.

## 📁Project Structure

- **algorithm.py:** Contains the implementation of SIFT, AKAZE, and ORB algorithms for keypoint detection and feature
  matching.
- **inference.py:** Script for running inference on two images using one of the matching algorithms.
- **processed_tci_images/:** Directory with preprocessed images used in this project.
- **demo.ipynb:** Jupyter Notebook that demonstrates the inference results of the image matching algorithm using SIFT,
  AKAZE, and ORB. It showcases the performance of each algorithm on satellite images, visualizes the matched keypoints,
  and compares the efficiency and accuracy of each method.
- **dataset_processing.ipynb:** Jupyter notebook that explains the preprocessing of the Sentinel-2 images and prepares
  the dataset for keypoint detection.
- **improvements_report.pdf:** This file outlines potential improvements for the project.

# 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.



