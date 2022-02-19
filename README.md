# Facial Recognition
This was done to try out facial recognition capabilities of Python, using face_recognition and PIL libraries.
The code can be modified to try images of any person by simply uploading the image and modifying the image path in the Python file.

## Identify Faces
File: IndentifyFaces.py

Identifies all faces in a group image by comparing it to known images of individuals. Then, on the group picture, draws a box around each person's face and labels it. If the face is recognized (in the known images), labels the box with their name, otherwise uses "Unknown".
