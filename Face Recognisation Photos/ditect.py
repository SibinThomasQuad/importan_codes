# import the libraries
import os
import face_recognition
from PIL import Image
image_to_be_matched = face_recognition.load_image_file('k.jpeg')
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
current_image = face_recognition.load_image_file('U.jpg')
current_image_encoded = face_recognition.face_encodings(current_image)[0]
result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
if result[0] == True:
    #line
    print("Matched:")
else:
    print("Not Matched:")
