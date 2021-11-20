import sys
import cv2 as cv
import numpy as np


#filePath = sys.argv[1]
# Load image:
# image = cv.imread(filePath)
# #convert image into greyscale mode
# gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# #find threshold of the image
# _, thrash = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY)
# contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)


def find_sqr_rect(filePath): 
    image = cv.imread(filePath)
    #convert image into greyscale mode
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #find threshold of the image
    _, thrash = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        shape = cv.approxPolyDP(contour, 0.02*cv.arcLength(contour, True), True)
        x_cor = shape.ravel()[0]
        y_cor = shape.ravel()[1]
        
        if len(shape) ==4:
            #shape cordinates
            x,y,w,h = cv.boundingRect(shape)

            #width:height
            aspectRatio = float(w)/h
            cv.drawContours(image, [shape], 0, (0,255,0), 4)
            if aspectRatio >= 0.9 and aspectRatio <=1.1:
                cv.putText(image, "Square", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
            else:
                cv.putText(image, "Rectangle", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
            
    cv.imshow("Square and Rectangles", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_triangle(filePath):
    image = cv.imread(filePath)
    #convert image into greyscale mode
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #find threshold of the image
    _, thrash = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        shape = cv.approxPolyDP(contour, 0.02*cv.arcLength(contour, True), True)
        x_cor = shape.ravel()[0]
        y_cor = shape.ravel()[1]

        #For triangle
        if len(shape) ==3:
            cv.drawContours(image, [shape], 0, (0,255,0), 4)
            cv.putText(image, "Triangle", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

                
    cv.imshow("Triangles", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_pentagon(filePath):
    image = cv.imread(filePath)
    #convert image into greyscale mode
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #find threshold of the image
    _, thrash = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        shape = cv.approxPolyDP(contour, 0.02*cv.arcLength(contour, True), True)
        x_cor = shape.ravel()[0]
        y_cor = shape.ravel()[1]

        #For pentagon
        if len(shape) ==5:
            cv.drawContours(image, [shape], 0, (0,255,0), 4)
            cv.putText(image, "Pentagon", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

                
    cv.imshow("Pentagon", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_circle(filePath):
    image = cv.imread(filePath)
    #convert image into greyscale mode
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #find threshold of the image
    _, thrash = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
        x_cor = shape.ravel()[0]
        y_cor = shape.ravel()[1]-15
        
        if len(shape) >12:
            cv.drawContours(image, [shape], 0, (0,255,0), 4)
            cv.putText(image, "Circle", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

                
    cv.imshow("circle", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_hexagon(filePath):
    image = cv.imread(filePath)
    #convert image into greyscale mode
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #find threshold of the image
    _, thrash = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        shape = cv.approxPolyDP(contour, 0.02*cv.arcLength(contour, True), True)
        x_cor = shape.ravel()[0]
        y_cor = shape.ravel()[1]
        
        if len(shape) == 6:
            cv.drawContours(image, [shape], 0, (0,255,0), 4)
            cv.putText(image, "Hexagon", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

                
    cv.imshow("Hexagon", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# if __name__ == "__main__":
    #img = image.copy()
    # user_input = input("""Options:
    #                     a : to classify Squares and Rectangles\n 
    #                     b : to classify Triangles\n  
    #                     c : to classify Pentagons\n
    #                     d : to classify Cirles\n
    #                     e : to classify Hexagon\n

    #                     Answer: """)

    # if user_input == 'a' :
    #     find_sqr_rect(img)
    # elif user_input == 'b':
    #     find_triangle(img)
    # elif user_input == 'c':
    #     find_pentagon(img)
    # elif user_input == 'd':
    #     find_circle(img)
    # elif user_input == 'e':
    #     find_hexagon(img)
