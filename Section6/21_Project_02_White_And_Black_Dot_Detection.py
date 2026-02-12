import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/black-dot1.jpg')
img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th, thresh_binary = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cnts = cv.findContours(thresh_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]

s1 =3
s2 = 120
xcnts = []

for c in cnts:
    area = cv.contourArea(c)
    if s1 < area < s2:
        print(area)
        xcnts.append(c)
        
print()
print(f'Total Contours Detected: {len(cnts)}')
print(f'Contours after filtering: {len(xcnts)}')

cv.drawContours(img, xcnts, -1, (0,255,0), 2)
cv.imshow('Detected White and Black Dots', img)
cv.waitKey(0)
cv.destroyAllWindows()
quit()



