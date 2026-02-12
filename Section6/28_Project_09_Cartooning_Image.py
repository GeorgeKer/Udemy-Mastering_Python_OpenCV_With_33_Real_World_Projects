import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

color = cv.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_blurred = cv.medianBlur(gray, 7)

edges = cv.adaptiveThreshold(gray_blurred, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=9, C=12)

cartoon = cv.bitwise_and(color, color, mask=edges)
cv.imshow('Cartoonized Image', cartoon)
cv.waitKey(0)

cv.destroyAllWindows()
quit()