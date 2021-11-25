import cv2 as cv
import matplotlib.pyplot as plt

def ss1(img):
    
    #img = cv.imread('ss1.jpeg')
    point_list = []
    point_list.append(((88, 28), (230, 157), 'saseendran'))
    point_list.append(((372, 38), (527, 150), 'inamul'))
    point_list.append(((697, 19), (858, 156), 'numan'))
    point_list.append(((59, 222), (219, 354), 'mahmuda'))
    point_list.append(((375, 231), (524, 344), 'gavin'))
    point_list.append(((675, 212), (819, 328), 'azureen'))
    point_list.append(((48, 371), (180, 467), 'JC'))
    point_list.append(((381, 383), (543, 512), 'goke'))
    point_list.append(((698, 393), (817, 511), 'afiq'))


    
    count=1
    a,b = 3,3
    for v in point_list:
        ((x1, y1), (x2, y2), label) = v

        if y2 < y1:
            x =x2
            x2 = x1
            x1 = x

        img_cropped = img[y1:y2, x1:x2].copy()
        
        print(img_cropped.shape)
        
        #cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv.imwrite('../../dataset/ss1/'+label+'.png',img_cropped)

        imgRGB = img_cropped[:, :, ::-1]
        plt.subplot(a, b, count)
        plt.imshow(imgRGB)
        count+=1

    # imgRGB = img_cropped[:, :, ::-1]
    # plt.subplot(1, 2, 2)
    # plt.imshow(imgRGB)

    plt.show()

def ss2(img):
    
    #img = cv.imread('ss2.jpg')
    point_list = []
    point_list.append(((102, 29), (177, 96), 'inamul'))
    point_list.append(((254, 24), (356, 99), 'goke'))
    point_list.append(((473, 16), (571, 89), 'azureen'))
    point_list.append(((81, 131), (159, 214), 'afiq'))
    point_list.append(((291, 124), (368, 206), 'numan'))
    point_list.append(((467, 130), (568, 220), 'mahmuda'))
    
    count=1
    a,b = 2,3
    for v in point_list:
        ((x1, y1), (x2, y2), label) = v

        if y2 < y1:
            x =x2
            x2 = x1
            x1 = x

        img_cropped = img[y1:y2, x1:x2].copy()
        
        print(img_cropped.shape)
        
        #cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv.imwrite('../../dataset/ss2/'+label+'.png',img_cropped)

        imgRGB = img_cropped[:, :, ::-1]
        plt.subplot(a, b, count)
        plt.imshow(imgRGB)
        count+=1

    # imgRGB = img_cropped[:, :, ::-1]
    # plt.subplot(1, 2, 2)
    # plt.imshow(imgRGB)

    plt.show()

def ss3(img):
    
    #img = cv.imread('ss3.jpg')
    point_list = []
    point_list.append(((115, 60), (227, 148), 'numan'))
    point_list.append(((342, 62), (484, 164), 'afiq'))
    point_list.append(((637, 52), (754, 167), 'saseendran'))
    point_list.append(((849, 59), (1013, 185), 'mahmuda'))
    point_list.append(((99, 224), (210, 326), 'gavin'))
    point_list.append(((360, 207), (463, 310), 'azureen'))
    point_list.append(((606, 209), (746, 317), 'inamul'))
    point_list.append(((849, 202), (998, 298), 'JC'))
    point_list.append(((116, 354), (230, 462), 'goke'))

    count=1
    a,b = 3,3
    for v in point_list:
        ((x1, y1), (x2, y2), label) = v

        if y2 < y1:
            x =x2
            x2 = x1
            x1 = x

        img_cropped = img[y1:y2, x1:x2].copy()
        print(img_cropped.shape)
        #cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv.imwrite('../../dataset/ss3/'+label+'.png',img_cropped)

        imgRGB = img_cropped[:, :, ::-1]
        plt.subplot(a, b, count)
        plt.imshow(imgRGB)
        count+=1

    # imgRGB = img_cropped[:, :, ::-1]
    # plt.subplot(1, 2, 2)
    # plt.imshow(imgRGB)

    plt.show()

if __name__ == '__main__':
    img1 = cv.imread("ss1.jpeg")
    img2 = cv.imread("ss2.jpg")
    img3 = cv.imread("ss3.jpg")
    ss1(img1)
    ss2(img2)
    ss3(img3)