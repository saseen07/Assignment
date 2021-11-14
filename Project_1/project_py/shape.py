import sys
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale:
filePath = sys.argv[1]
# Load image:
img = cv.imread(filePath)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# plt.figure(figsize=(12,8))



# BGR to RGB
# imgRGB = img[:,:,::-1]
# plt.subplot(221)
# plt.imshow(imgRGB)

# Apply thresholding to get a binary image:
ret, threshImg = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)


# gray to RGB
# imgRGB = cv.cvtColor(threshImg, cv.COLOR_GRAY2RGB)
# plt.subplot(222)
# plt.imshow(imgRGB)

# Find contours using the thresholded image:
contours, hierarchy = cv.findContours(threshImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# number of detected contours:
print(f"detected contours: {len(contours)}")

# approxPolyDP():
imgApproxPolyDP = img.copy()
for contour in contours:
    perimeter = cv.arcLength(contour, True)
    epsilon = 0.03 * perimeter
    approxPolyDP = cv.approxPolyDP(contour, epsilon, True)

    
    color = (0, 255, 255)
    thickness = 5
    # draw line
    for approx in approxPolyDP:
        cv.drawContours(imgApproxPolyDP, [approx], 0, color, thickness)
    color = (255, 255, 255)
    thickness = 5
    # draw points
    for approx in [approxPolyDP]:
        # draw points
        squeeze = np.squeeze(approx)
        print('contour:',approx.shape, squeeze.shape)
        for p in squeeze:
            pp = tuple(p.reshape(1, -1)[0])
            cv.circle(imgApproxPolyDP, pp, 10, color, -1)


    # determine shape   
    verticeNumber = len(approxPolyDP)
    if verticeNumber == 3:
        vertice_shape = (verticeNumber, 'Triangle')
    elif verticeNumber == 4:
        # get aspect ratio
        x, y, width, height = cv.boundingRect(approxPolyDP)
        aspectRatio = float(width) / height
        #print(aspectRatio)
        if 0.90 < aspectRatio < 1.1: 
            vertice_shape = (verticeNumber, 'Square')
        else:
            vertice_shape = (verticeNumber, 'Rectangle')
    elif verticeNumber == 5:
        vertice_shape = (verticeNumber, 'Pentagon')
    elif verticeNumber == 6:
        vertice_shape = (verticeNumber, 'Hexagon')
    elif verticeNumber == 7:
        vertice_shape = (verticeNumber, "Heptagon")
    else:
        vertice_shape = (verticeNumber, 'Circle')
#     elif verticeNumber == 8:
#         vertice_shape = (verticeNumber, "Octagon")
#     elif verticeNumber == 9:
#         vertice_shape = (verticeNumber, "Nonagon")
#     elif verticeNumber == 10:
#         vertice_shape = (verticeNumber, "Decagon")
        
    
    # write shape
    # Compute the moment of contour:
    M = cv.moments(contour)

    # The center or centroid can be calculated as follows:
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    # Get the position to draw:    
    text = vertice_shape[1]
    fontFace = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    thickness = 3
    text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

    text_x = cX - text_size[0] / 2
    text_x = round(text_x)
    text_y = cY + text_size[1] / 2
    text_y = round(text_y)
    
    # Write the ordering of the shape on the center of shapes
    color = (0, 0, 0)
    cv.putText(imgApproxPolyDP, text, (text_x, text_y), fontFace, fontScale, color, thickness)
    
cv.imshow("Original", img)


k = cv.waitKey(0)
x = cv.waitKey(0)
if k == ord("q"):
    cv.imshow("Thresh_Image", threshImg)
    x = cv.waitKey(0)

if x == ord("s"):
    cv.imshow("Sorted", imgApproxPolyDP)
    y = cv.waitKey(0)


cv.destroyAllWindows()
# BGR to RGB
# imgRGB = imgApproxPolyDP[:,:,::-1]
# plt.subplot(223)
# plt.imshow(imgRGB)

# plt.show()