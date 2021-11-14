import sys
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale:
filePath = sys.argv[1]
# Load image:
img = cv.imread(filePath)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(imgGray[400,600])
# Apply thresholding to get a binary image:
ret, threshImg = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)

# Find contours using the thresholded image:
contours, hierarchy = cv.findContours(threshImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# number of detected contours:
print(f"detected contours: {len(contours)}")

# create list of tuple (size, shape) for each contour
# list of contour size
contours_sizes = [cv.contourArea(contour) for contour in contours]
# list of (size, contour)
size_shape_list = zip(contours_sizes, contours)
sorted_size_shape_list = sorted(size_shape_list)
# (contour_sizes, contours) = zip(*sorted_size_shape_list)

cv.imshow("Original", img)

# # BGR to RGB
# imgRGB = img[:,:,::-1]
# plt.subplot(211)
# plt.imshow(imgRGB)

for i, (size, contour) in enumerate(sorted_size_shape_list):
    # Compute the moment of contour:
    M = cv.moments(contour)

    # The center or centroid can be calculated as follows:
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    # Get the position to draw:    
    text = str(i + 1)
    fontFace = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    thickness = 3
    text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

    text_x = cX - text_size[0] / 2
    text_x = round(text_x)
    text_y = cY + text_size[1] / 2
    text_y = round(text_y)
    
    # Write the ordering of the shape on the center of shapes
    color = (0, 0, 0)
    cv.putText(img, text, (text_x, text_y), fontFace, fontScale, color, thickness)




k = cv.waitKey(0)

if k != ord("q"):
    cv.imshow("Sorted", img)
    y = cv.waitKey(0)


cv.destroyAllWindows()
# BGR to RGB
# imgRGB = img[:,:,::-1]
# plt.subplot(212)
# plt.imshow(imgRGB)

# plt.show()