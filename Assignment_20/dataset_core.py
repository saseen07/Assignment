'''
Class Activity
1. Download 5 images from internet
2. Name the 5 images with suffix _A _B _A _C _C
3. Extract the images and same to a list with corresponding labels in another list
'''
'''
Class Activity
1. Save the list of images and labels using 'np.savez_compressed(datasetfilename, images=images, labels=labels)'
2. Load the dataset in another module or file called test.py and display the third image label
'''

# Creation of dataset

import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def create_dataset(datasetfilename, srcPaths, classNames):

    # List of images
    imgList = []
    labelList = []
    labelNameList = []

    # Read image files from folder

    for srcPath in srcPaths:
        for fname in sorted(os.listdir(srcPath)):
            filePath = os.path.join(srcPath, fname)
            img = cv.imread(filePath)

            # Get label
            fname_wo_ext = os.path.splitext(fname)[0]
            # label = fname_wo_ext[-1] # if label is the end of file name e.g.: Image_A.png, Image_B.png
            label = fname_wo_ext # if label is the whole file name e.g.: numan.png, afiq.png

            imgList.append(img)
            labelList.append(classNames[label])
            labelNameList.append(label)
            # print(fname)

    # Save dataset

    images = np.array(imgList, dtype='object')
    labels = np.array(labelList)
    labelnames = np.array(labelNameList) # new 
    
    np.savez_compressed(datasetfilename, images=images, labels=labels, labelnames=labelnames)

    return True
    # return imgList, labelList
