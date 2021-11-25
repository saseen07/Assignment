from dataset_core import create_dataset
import numpy as np
import matplotlib.pyplot as plt

srcPaths = ['dataset/ss1','dataset/ss2','dataset/ss3']
dataSetFilename = 'cvdataset.npz'
if create_dataset(dataSetFilename,srcPaths):

    data = np.load(dataSetFilename, allow_pickle=True)
    imgList = data['images']
    labelList = data['label']
    for i in range (24):
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
