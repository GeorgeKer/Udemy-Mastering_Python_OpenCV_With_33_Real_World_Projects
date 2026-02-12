import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt    

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
img_resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))   
gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
_, thresh_binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, thresh_binary_inv = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
_, thresh_trunc = cv.threshold(gray, 180, 255, cv.THRESH_TRUNC)
_, thresh_tozero = cv.threshold(img_resized, 37, 255, cv.THRESH_TOZERO)
_, thresh_tozero_inv = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO_INV)

adaptive_thresh_mean = cv.adaptiveThreshold(gray, 200, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 200, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Original Image', img_resized)
# cv.imshow('Grayscale Image', gray)
# cv.imshow('Threshold Binary', thresh_binary)        
# cv.imshow('Threshold Binary Inverse', thresh_binary_inv):
cv.imshow('Threshold Trunc', thresh_trunc)
cv.imshow('Threshold To Zero', thresh_tozero)
# cv.imshow('Threshold To Zero Inverse', thresh_tozero_inv)

cv.imshow('Adaptive Threshold Mean', adaptive_thresh_mean)
# cv.imshow('Adaptive Threshold Gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)
cv.destroyAllWindows()
quit()
