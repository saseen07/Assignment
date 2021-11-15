import cv2 as cv
import sys

# add samples data path to cv
filePath = sys.argv[1]
# Load image:
img = cv.imread(filePath)
# check if file found
if img is None:
    sys.exit("Could not read the image.")

# display file
cv.imshow("Display window", img)

# pause execution here by waiting for a user to press a key
k = cv.waitKey(0)

cv.destroyAllWindows()