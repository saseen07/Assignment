import cv2 as cv
import matplotlib.pyplot as plt
import os

imgFile = 'ss1.jpeg'
img = cv.imread(imgFile)

if not os.path.exists("dataset"):
    os.mkdir("dataset")


folderPath = os.path.splitext(imgFile)[0]
folderPath =f"../dataset/{folderPath}"

if not os.path.exists("dataset"):
    os.mkdir(folderPath)

point_list_of_list = []
point_list = []
point_list.append(((88, 28), (230, 157), 'saseen'))
point_list.append(((372, 38), (527, 150), 'inamul'))
point_list.append(((697, 19), (858, 156), 'numan'))
point_list.append(((59, 222), (219, 354), 'mahmuda'))
point_list.append(((375, 231), (524, 344), 'gavin'))
point_list.append(((675, 212), (819, 328), 'azureen'))
point_list.append(((48, 371), (180, 467), 'JC'))
point_list.append(((381, 383), (543, 512), 'goke'))
point_list.append(((698, 393), (817, 511), 'afeeq'))
point_list_of_list.append(point_list)

point_list2 = []
point_list2.append(((102, 29), (177, 96), 'inamul'))
point_list2.append(((254, 24), (356, 99), 'goke'))
point_list2.append(((473, 16), (571, 89), 'azureen'))
point_list2.append(((81, 131), (159, 214), 'afeeq'))
point_list2.append(((291, 124), (368, 206), 'numan'))
point_list2.append(((467, 130), (568, 220), 'mahmuda'))
point_list_of_list.append(point_list2)


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
    saveFilepath = folderPath +'/'+label+'.png'
    #cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv.imwrite(saveFilepath,img_cropped)

    imgRGB = img_cropped[:, :, ::-1]
    plt.subplot(a, b, count)
    plt.imshow(imgRGB)
    count+=1

# imgRGB = img_cropped[:, :, ::-1]
# plt.subplot(1, 2, 2)
# plt.imshow(imgRGB)

plt.show()