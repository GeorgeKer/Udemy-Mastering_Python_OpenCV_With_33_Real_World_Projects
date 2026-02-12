import os
import cv2

img_path = os.path.expanduser("~/INPUT/TEST_IMAGE.jpg")
img = cv2.imread(img_path)

if img is None:
	raise FileNotFoundError(f"Image not found: {img_path}")

cv2.imshow('test_window', img)
cv2.waitKey(0)