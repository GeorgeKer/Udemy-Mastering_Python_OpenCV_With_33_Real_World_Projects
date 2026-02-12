import cv2 as cv
import numpy as np
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 10, (0, 255, 0), -1)


cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_circle)

while True:
    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
quit()