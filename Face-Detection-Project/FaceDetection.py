import cv2
from cv2 import face
import numpy as np
from random import randrange as r

# Load the cascade
face_cascade = cv2.CascadeClassifier(r'H:\Python\Face Detection Pyton\face.xml')
"""
# To capture video from webcam. 
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    cap.release()  # Ensure the capture object is released
    cv2.destroyAllWindows()  # Close any OpenCV windows
    exit()

while True:
    # Read the frame
    ret, img = cap.read()

    # Check if frame is captured correctly
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (r(0, 256), r(0, 256), r(0, 256)), 3)

    # Display the resulting image
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # ESC key
        break

# Release the VideoCapture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
"""


# Static image face detection
# Load the image (ensure the path is correct)
img = cv2.imread(r'H:\Python\Face Detection Pyton\img2.jpg')

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to grayscale
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faceCoordinates = face_cascade.detectMultiScale(grayimg)

# Draw rectangles around the detected faces
for (x, y, w, h) in faceCoordinates:
    cv2.rectangle(img, (x, y), (x + w + 2, y + h + 10), (r(0, 256), r(0, 256), r(0, 256)), 3)

# Display the image with rectangles around faces
cv2.imshow('Detect Face', img)

# Wait for any key press to close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()

print('End of program')
