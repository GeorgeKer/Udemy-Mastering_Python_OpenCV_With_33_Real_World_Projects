import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
kernel = (5, 5)
img = cv.imread(img_path)


blur = cv.blur(img, kernel)
gaussian = cv.GaussianBlur(img, kernel, 0)
median = cv.medianBlur(img, 5)
bilateral = cv.bilateralFilter(img, 9, 75, 75)

# cv.imshow('Original', img)
# cv.imshow('Averaging', blur)
cv.imshow('Gaussian Blurring', gaussian)
# cv.imshow('Median Blurring', median)
# cv.imshow('Bilateral Blurring', bilateral)
cv.waitKey(0)
cv.destroyAllWindows()
quit()