import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
img_resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))

circle = np.zeros(img_resized.shape, dtype=np.uint8)
circle = cv.circle(circle, (img_resized.shape[1]//2, img_resized.shape[0]//2), 200, (255, 255, 255), -1)
# rectangle = np.zeros(img_resized.shape, dtype=np.uint8)
# rectangle = cv.rectangle(rectangle, (50, 50), (img_resized.shape[1]-50, img_resized.shape[0]-50), (255, 255, 255), -1)

bitwise_and = cv.bitwise_and(img_resized, circle)
bitwise_or = cv.bitwise_or(img_resized, circle)
# bitwise_xor = cv.bitwise_xor(img_resized, circle)
bitwise_xor = cv.bitwise_xor(img_resized, circle)
bitwise_not = cv.bitwise_not(img_resized, circle)

cv.imshow('Bitwise AND', bitwise_and)
cv.imshow('Bitwise OR', bitwise_or)
cv.imshow('Bitwise XOR', bitwise_xor)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()
quit()