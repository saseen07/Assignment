import cv2 as cv
  
# Load the cascade  
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')  
  
# To capture video from webcam.   
cap = cv.VideoCapture(0)  

fourcc = cv.VideoWriter_fourcc(*'XVID')
video_out = cv.VideoWriter('test.mp4', fourcc, 20.0, (640,  480)) 
while True:  
    
    # Read the frame  
    _, img = cap.read()  
  
    # Convert to grayscale  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
  
    # Detect the faces  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
    
    video_out.write(img)
    # Display  
    cv.imshow('Video', img)  
    
   
    # Stop if escape key is pressed  
    k = cv.waitKey(1) 
    # check if key is q then exit
    if k == ord("q"):
        break 
          
# Release the VideoCapture object  
cap.release()  
video_out.release()
cv.destroyAllWindows()
 