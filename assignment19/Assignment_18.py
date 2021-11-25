# see load_label_png.py also.
import numpy as np
import PIL.Image
import cv2 as cv

label_png = 'ss1_json/label_viz.png'
lbl = np.asarray(PIL.Image.open(label_png))
print(lbl.dtype)
print(np.unique(lbl))
print(lbl.shape)

# img=cv.imread(label_png)
# cv.imshow('image',img)
# k = cv.waitKey(0)

# cv.destroyAllWindows()
