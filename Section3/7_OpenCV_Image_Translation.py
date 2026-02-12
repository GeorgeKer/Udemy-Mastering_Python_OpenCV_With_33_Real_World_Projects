import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)

def img_translation(img, x, y):
    M_ = np.float32([[1,0,x], [0,1,y]])
    dimention = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, M_, dimention)

img_test = img_translation(img, -100, 100)
cv.imshow('Test', img_test)

cv.waitKey(0)
cv.destroyAllWindows()
quit()