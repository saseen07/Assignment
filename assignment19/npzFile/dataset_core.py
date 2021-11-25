import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def create_dataset(dataSetFilename,srcPaths):
    
    # list of images
    imgList = []
    labelList = []

    # read image files from folder 
    for srcPath in srcPaths:
        for fname in os.listdir(srcPath):
            filePath = os.path.join(srcPath, fname)
            img = cv.imread(filePath)

            #get last character 
            fname_no_ext = os.path.splitext(fname)[0]
            #label = fname_no_ext[-1]
            label = fname_no_ext
        
        # append image
            imgList.append(img)
            labelList.append(label)
        
    # save dataset
    

    images = np.array(imgList, dtype='object')
    labels = np.array(labelList, dtype='object')
    np.savez_compressed(dataSetFilename, images=images, label=labels)
    
    return True
    #return imgList,labelList

if __name__ == "__main__":
    #imgList, labelList= create_dataset()
    dataSetFilename = 'saseendataset.npz'
    if create_dataset(dataSetFilename):

        data = np.load(dataSetFilename, allow_pickle=True)
        imgList = data['images']
        labelList = data['label']
        for i in range (5):
            #display first and second image
            img = imgList[i]
            label = labelList[i]
            # convert bgr to rgb
            imgRGB = img[:,:,::-1]
            # show
            
            plt.imshow(imgRGB)
            plt.title(label)
            # show
            plt.show()

    # img = imgList[1]
    # label = labelList[1]
    # # convert bgr to rgb
    # imgRGB = img[:,:,::-1]
    # # show
    # plt.imshow(imgRGB)
    # plt.title(label)
    # # show
    # plt.show()

    # img = imgList[2]
    # label = labelList[2]
    # # convert bgr to rgb
    # imgRGB = img[:,:,::-1]
    # # show
    # plt.imshow(imgRGB)
    # plt.title(label)
    # # show
    # plt.show()

    # img = imgList[3]
    # label = labelList[3]
    # # convert bgr to rgb
    # imgRGB = img[:,:,::-1]
    # # show
    # plt.imshow(imgRGB)
    # plt.title(label)
    # # show
    # plt.show()

    # img = imgList[4]
    # label = labelList[4]
    # # convert bgr to rgb
    # imgRGB = img[:,:,::-1]
    # # show
    # plt.imshow(imgRGB)
    # plt.title(label)
    # # show
    # plt.show()
