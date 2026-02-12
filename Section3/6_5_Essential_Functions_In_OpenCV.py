import cv2 as cv
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)

# 1
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Test 5 Functions', grey)

# 2
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Test', blur)

# 3
cany = cv.Canny(img, 40, 250)
# cv.imshow('Test 3', cany)

# 4
dilated = cv.dilate(cany, (3, 3), iterations=5)
# cv.imshow('Test 4', dilated)

# 5
resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
cropped = resized[100:400, 200:500]
cv.imshow('Test 5', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
quit()