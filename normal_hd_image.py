#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Open a connection to the camera
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture 10 images
for i in range(10):
    # Capture a single frame
    ret, frame = camera.read()

    # Check if the frame was captured successfully
    if ret:
        # Save the captured image to a file
        filename = f"captured_image_{i+1}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image {i+1} captured and saved successfully.")
    else:
        print(f"Error: Could not capture image {i+1}.")

# Release the camera
camera.release()

# Close any OpenCV windows
cv2.destroyAllWindows()

