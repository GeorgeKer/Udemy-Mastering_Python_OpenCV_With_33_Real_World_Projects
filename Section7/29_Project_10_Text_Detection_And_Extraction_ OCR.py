import cv2 as cv
import numpy as np 
import os
import pytesseract

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE_WITH_TEXT.png')
img = cv.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
extracted_text = pytesseract.image_to_string(gray)
print("Extracted Text:")
print(extracted_text)

cv.imshow('Original Image', img)
cv.imshow('Grayscale Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()
quit()