from dataset_core import create_dataset
import matplotlib.pyplot as plt
import numpy as np
import labelme2coco

srcPaths = ['dataset/ss1', 'dataset/ss2', 'dataset/ss3']
# srcPaths = ['rawdata/camera']
datasetfilename = 'saseendataset.npz'

classNames = {'afiq': 0,'azureen': 1,'gavin': 2,'goke': 3,'inamul': 4,'JC': 5,'mahmuda': 6,'numan': 7,'saseendran': 8}

# classNames = {'A': 0, 'B': 1, 'C': 2}

if create_dataset(datasetfilename, srcPaths, classNames):

    data = np.load(datasetfilename, allow_pickle=True)
    imgList = data['images']
    labelList = data['labels']
    labelNameList = data['labelnames'] #new

    print(f'{imgList.shape = }')
    print(f'{labelList.shape = }')

    # Display 3rd image and label
    i = 0
    img = imgList[i]
    label = labelList[i]
    labelName = labelNameList[i]
    print(labelList)

    # Convert BGR to RGB

    imgRGB = img[:, :, ::-1]

    # Show image
    plt.imshow(imgRGB)
    plt.title(f'{label} : {labelName}')
    plt.axis('off')
    plt.show()
