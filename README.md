# Facial Recognition Model using OpenCV

### Project Overview
This code is a simple Python program that demonstrates face detection and landmark detection using the Dlib library and OpenCV. The folder also has an `EyeDetection.ipynb` file that only tracks your eyes, instead of your whole face.

The goal of the project is to detect and visualize facial landmarks in real-time using a webcam. It uses Dlib's facial landmark detection to identify and annotate specific facial features in the video stream, such as the corners of the mouth, the eyebrows, and the eyes.

This project can be used for a variety of applications, including emotion recognition, head pose estimation, and face recognition. By identifying key facial landmarks, this project can enable more advanced analysis of facial expressions and head orientation, which can be useful for a variety of fields such as computer vision, psychology, and human-computer interaction.

##### Libraries and versions used
Library         | Version | Installation Command
--------------- | ------- | --------------------
Python          | 3.x     | -
OpenCV-Python   | 4.x     | pip install opencv-python
MediaPipe     | 0.9.1   | pip install mediapipe
Dlib       | 19.24.0  | pip install dlib

### Running the script
1. Clone the repository to your local machine
    ```bash
    git clone https://github.com/Nicolas-Formenton/Facial_Detection_Model_ML.git
    ```
2. Change into the directory of the cloned repository
    ```bash 
    cd Facial_Detection_Model_ML
    ```
3. Install the required libraries
    ```bash
    python -m pip install -r requirements.txt
    ```
4. Have Jupyter Notebook installed and then run the cells you want to test.

### Code Explanation
The code is written in Python and uses the following libraries:

Library         | Usage   |
--------------- | ------- | 
OpenCV          | Used for image processing tasks, such as converting the image to grayscale and applying thresholding.| 
MediaPipe |  Framework for building multi-modal applied machine learning pipelines. It enables quick and easy prototyping and deployment of computer vision and machine learning models.
Dlib |  Library that provides a wide range of tools for developing software with machine learning, computer vision, and image processing capabilities. It includes algorithms and techniques for tasks such as face detection, object detection and tracking, image transformation, and clustering.

This is a Python code that captures video from a webcam, detects faces using the dlib frontal face detector, and then extracts 68 facial landmarks using the dlib shape predictor. It uses OpenCV to display the video and overlay the detected landmarks on top of the face regions.

The code starts by importing the necessary libraries: OpenCV and dlib. It initializes the dlib frontal face detector and shape predictor using pre-trained models, then starts capturing video from the default camera.

In the main loop, it reads each frame of the video and converts it to grayscale. It then detects faces in the grayscale frame using the frontal face detector, and for each face detected, it extracts the 68 facial landmarks using the shape predictor. The code then draws a green circle on each of the 68 landmarks, effectively creating a facial landmark heatmap.

It also displays the number of faces detected in the current frame in red text at the top left corner of the video window. The loop continues until the user presses the 'q' key, at which point the program exits and the resources are released.

###### Future Developments
###### I want to be able to use this project as a starting point to somehow be able to track my facial expressions and eye movements and use it in a practical way, maybe being able to visualize where I'm looking at my computer screen, or maybe do some mouse movements with it, etc...