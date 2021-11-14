import sys
import cv2 as cv
import matplotlib.pyplot as plt
  
# Load the cascade  
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')  

filePath = sys.argv[1]
# To capture video from existing video.   
cap = cv.VideoCapture(filePath)  
  
while True:  
    # Read the frame  
    _, img = cap.read()  
  
    # Convert to grayscale  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
  
    # Detect the faces  
    faces = face_cascade.detectMultiScale(gray, 2, 1)  
  
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
  
    # Display  
    cv.imshow('Video', img)  
  
    # Stop if escape key is pressed  
    k = cv.waitKey(5) 
    # check if key is q then exit
    if k == ord("q"):
        break
          
# Release the VideoCapture object  
cap.release()  
cv.destroyAllWindows()