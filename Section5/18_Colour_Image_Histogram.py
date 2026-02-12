import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
img_resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img_resized], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    # plt.xlim([0, 256])

cv.imshow('Original Image', img_resized)
plt.show()  

cv.waitKey(0)
cv.destroyAllWindows()
quit()