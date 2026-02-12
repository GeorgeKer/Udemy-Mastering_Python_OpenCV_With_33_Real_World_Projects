import cv2 as cv
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
img_resized = cv.resize(img, (2*img.shape[1]//3, 2*img.shape[0]//3))
# cv.imshow('Original Image', img)

img_gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)

for i in range(125, 255, 5):
    ret, img_canvas = cv.threshold(img_gray, i, 255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(img_canvas, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(contours[-1])
    img_canvas = cv.drawContours(img_resized, contours, -1, (0, 255, 0), 1)
    cv.imwrite(f'{i}.png', img_canvas)

cv.waitKey(0)
cv.destroyAllWindows()
quit()