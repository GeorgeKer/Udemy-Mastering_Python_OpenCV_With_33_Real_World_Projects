import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
img_resized = cv.resize(img, (2*img.shape[1]//3, 2*img.shape[0]//3))
# cv.imshow('Original Image', img)

gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
edges = cv.Canny(blurred, 50, 150)
hsv = cv.cvtColor(img_resized, cv.COLOR_BGR2HSV)
rgb = cv.cvtColor(img_resized, cv.COLOR_BGR2RGB)
lab = cv.cvtColor(img_resized, cv.COLOR_BGR2Lab)

cv.imshow('Grayscale', gray)
cv.imshow('Blurred', blurred)
cv.imshow('Canny Edges', edges)
cv.imshow('HSV Color Space', hsv)      
cv.imshow('RGB Color Space', rgb)
cv.imshow('Lab Color Space', lab)

cv.waitKey(0)
cv.destroyAllWindows()
quit()