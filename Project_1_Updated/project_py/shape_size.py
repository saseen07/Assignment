import sys
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale:
filePath = sys.argv[1]
# Load image:
img = cv.imread(filePath)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Apply thresholding to get a binary image:
ret, threshImg = cv.threshold(imgGray, 150, 255, cv.THRESH_BINARY_INV)

# Find contours using the thresholded image:
contours, hierarchy = cv.findContours(threshImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f"detected contours: {len(contours)}")


imgRGB = img[:,:,::-1]
plt.subplot(211)
plt.title("Original")
plt.imshow(imgRGB)

triangle = 0
rectangle = 0
square = 0
pentagon = 0
hexagon = 0
circle = 0

# approxPolyDP():
imgApproxPolyDP = img.copy()
for contour in contours:
    approxPolyDP = cv.approxPolyDP(contour, 0.02*cv.arcLength(contour, True), True)

    color = (0, 255, 255)
    thickness = 5
    
    # draw line
    for approx in approxPolyDP:
        cv.drawContours(imgApproxPolyDP, [approx], 0, color, thickness)
    color = (0, 0, 255)
    thickness = 5
    # draw points
    for approx in [approxPolyDP]:
        # draw points
        squeeze = np.squeeze(approx)
        #print('contour:',approx.shape, squeeze.shape)
        for p in squeeze:
            pp = tuple(p.reshape(1, -1)[0])
            cv.circle(imgApproxPolyDP, pp, 10, color, -1)
            
     # write shape
    # Compute the moment of contour:
    M = cv.moments(contour)

    # The center or centroid can be calculated as follows:
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    # determine shape   
    verticeNumber = len(approxPolyDP)
    if verticeNumber == 3:
        vertice_shape = (verticeNumber, 'Triangle')

        triangle+=1
        textTri = str(triangle)
        textShape = vertice_shape[1]
        text1 = textShape + textTri
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        thickness = 3
        text_size = cv.getTextSize(text1, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgApproxPolyDP, text1, (text_x, text_y), fontFace, fontScale, color, thickness)
        
    elif verticeNumber == 4:
        # get aspect ratio
        x, y, width, height = cv.boundingRect(approxPolyDP)
        aspectRatio = float(width) / height
        #print(aspectRatio)
        if aspectRatio >= 0.9 and aspectRatio <=1.1: 
            vertice_shape = (verticeNumber, 'Square')

            square+=1
            textSqu = str(square)
            textShape = vertice_shape[1]
            text2 = textShape + textSqu 
            fontFace = cv.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            thickness = 3
            text_size = cv.getTextSize(text2, fontFace, fontScale, thickness)[0]

            text_x = cX - text_size[0] / 2
            text_x = round(text_x)
            text_y = cY + text_size[1] / 2
            text_y = round(text_y)
            
            # Write the ordering of the shape on the center of shapes
            color = (0, 0, 0)
            cv.putText(imgApproxPolyDP, text2, (text_x, text_y), fontFace, fontScale, color, thickness)
        else:
            vertice_shape = (verticeNumber, 'Rectangle')

            rectangle +=1
            textRect = str(rectangle)
            textShape = vertice_shape[1]
            text3 = textShape + textRect 
            fontFace = cv.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            thickness = 3
            text_size = cv.getTextSize(text3, fontFace, fontScale, thickness)[0]

            text_x = cX - text_size[0] / 2
            text_x = round(text_x)
            text_y = cY + text_size[1] / 2
            text_y = round(text_y)
            
            # Write the ordering of the shape on the center of shapes
            color = (0, 0, 0)
            cv.putText(imgApproxPolyDP, text3, (text_x, text_y), fontFace, fontScale, color, thickness)

    elif verticeNumber == 5:
        vertice_shape = (verticeNumber, 'Pentagon')

        pentagon +=1
        textPen = str(pentagon)
        textShape = vertice_shape[1]
        text4 = textShape + textPen 
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        thickness = 3
        text_size = cv.getTextSize(text4, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgApproxPolyDP, text4, (text_x, text_y), fontFace, fontScale, color, thickness)

    elif verticeNumber == 6:
        vertice_shape = (verticeNumber, 'Hexagon')

        hexagon +=1
        textHex = str(hexagon)
        textShape = vertice_shape[1]
        text5 = textShape+ textHex 
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        thickness = 3
        text_size = cv.getTextSize(text5, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgApproxPolyDP, text5, (text_x, text_y), fontFace, fontScale, color, thickness)

    else:
        vertice_shape = (verticeNumber, 'Circle')

        circle +=1
        textCir = str(circle)
        textShape = vertice_shape[1]
        text5 = textShape + textCir 
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        thickness = 3
        text_size = cv.getTextSize(text5, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgApproxPolyDP, text5, (text_x, text_y), fontFace, fontScale, color, thickness)

imgRGB = imgApproxPolyDP[:,:,::-1]
plt.subplot(212)
plt.title("Sorted by shape then size")
plt.imshow(imgRGB)

plt.tight_layout()
plt.show()
