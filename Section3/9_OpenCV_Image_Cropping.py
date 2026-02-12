import cv2 as cv
import os
import numpy as np

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)

resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

flipped = cv.flip(resized, 1)
cv.imshow('Flipped', flipped)

cropped = img[0:500, 200:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
quit()