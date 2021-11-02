import sys
import cv2 as cv
import matplotlib.pyplot as plt

# get the file path from command line
filePath = sys.argv[1]
# get sample file path for "starry_night.jpg"
#filePath = "output.avi"

capture = cv.VideoCapture(filePath)

# check if connected
if capture.isOpened() is False:
    print("Error opening camera 0")
    exit()

while capture.isOpened():
    # capture frames, if read correctly ret is True
    ret, frame = capture.read()

    if not ret:
        print("Didn't receive frame. Stop ")
        break

    # display frame
    cv.imshow("Camera frame", frame)

    k = cv.waitKey(5)

    # check if key is q then exit
    if k == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
