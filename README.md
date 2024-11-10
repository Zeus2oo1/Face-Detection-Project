# Face Detection Project

This Python project performs face detection in real-time or on static images using OpenCV's Cascade Classifier. This face detection approach is based on Haar Feature-Based Cascade Classifiers, making it efficient for real-time applications.

## Description

### Key Libraries
- **OpenCV (cv2)**: An open-source computer vision library with powerful tools for image and video processing. 
- **NumPy (np)**: A library for numerical operations in Python, often used for handling arrays and matrices.
- **cv2.face**: OpenCV’s face module includes functions for face detection and recognition, providing additional models and algorithms related to facial recognition tasks.

### Haar Feature-Based Cascade Classifiers
Haar Cascades are used in this project to detect faces. Here’s a breakdown of how this method works:
- **Purpose**: A technique for object detection commonly used to identify objects in images or videos, specifically suited for face detection.
- **Training**: Built using a large dataset of positive (faces) and negative (non-face) images to train a series of weak classifiers, resulting in a highly accurate detection model.
- **Features**:
  - **Haar-like Features**: Simple rectangular features that capture differences in intensity.
  - **Integral Image**: Speeds up computation by using a summed-area table.
  - **Adaboost Algorithm**: Selects the most relevant features to form a strong classifier.
  - **Cascade Structure**: Organizes classifiers in stages, each refining the detection and improving efficiency.
  - **False Positive Control**: Trained to maintain high detection accuracy with low false positives.

## Installation

Clone the repository and install the dependencies listed in `requirements.txt`:

```bash
git clone https://github.com/Zeus2oo1/Face-Detection-Project.git
cd Face-Detection-Project
pip install -r requirements.txt
```

## Usage
Real-Time Face Detection (Webcam)
- Uncomment the VideoCapture code in face_detection.py.
- Run the following command:

      python face_detection.py

Static Image Face Detection
- Add your image file to the data folder and update the image path in face_detection.py.
- Run the following command:

      python face_detection.py
  
### Example Output

You’ll see detected faces outlined with rectangles, displayed in different colors.

## Requirements

    Python 3.x
    OpenCV
    NumPy
