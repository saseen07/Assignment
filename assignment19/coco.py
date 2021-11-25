# import package
import labelme2coco
import os
import cv2 as cv
from PIL import Image
import glob

imgList = []
labelList = []
srcPath = 'test'
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

# set path for coco json to be saved

for i in range(3):
    img = imgList[i]
    label = labelList[i]
    save_json_path = f"data/{label}.json"
    print(label)
    # convert labelme annotations to coco
    labelme2coco.convert(filePath, save_json_path)
