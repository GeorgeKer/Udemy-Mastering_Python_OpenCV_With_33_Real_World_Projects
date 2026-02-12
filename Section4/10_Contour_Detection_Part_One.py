import cv2 as cv
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)

img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred = cv.GaussianBlur(gray, (9, 9),cv.BORDER_DEFAULT)
cv.imshow('Blurred Image', blurred)

canny_blurred = cv.Canny(blurred, 150, 200)
cv.imshow('Canny Blurred to Original', canny_blurred)

cv.waitKey(0)
cv.destroyAllWindows()
quit()