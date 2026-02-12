import cv2 as cv
import os
import numpy as np

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)

def img_rotation(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    M_ = cv.getRotationMatrix2D(rot_point, angle, .7)
    dimention = (width, height)

    return cv.warpAffine(img, M_, dimention)


img_rotated = img_rotation(img, 35)
cv.imshow('Rotated Image', img_rotated)
cv.waitKey(0)
cv.destroyAllWindows()
quit()