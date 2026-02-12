import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
circle = cv.circle(np.zeros(gray.shape, dtype=np.uint8), (gray.shape[1]//2, gray.shape[0]//2), 100, (255), -1)
mask = cv.bitwise_and(gray, gray, mask=circle)

hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

cv.imshow('Original Image', img)

plt.figure()
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
quit()