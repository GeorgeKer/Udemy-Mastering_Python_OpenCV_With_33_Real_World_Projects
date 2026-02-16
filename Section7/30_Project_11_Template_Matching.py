import cv2 as cv
import os
import pytesseract

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
template_path = os.path.expanduser('~/INPUT/TEST_TEMPLATE_SHIP_CROP.png')
img = cv.imread(img_path, 0)
if img is None: raise FileNotFoundError(f"Image not found at path: {img_path}")

template  = cv.imread(template_path, 0)
if template is None: raise FileNotFoundError(f"Template image not found at path {template_path}")
h_temp, w_temp = template.shape

matching_methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCOEFF_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in matching_methods:
    img_copy = img.copy()
    result = cv.matchTemplate(img_copy, template, method)
    min_val , max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w_temp, location[1]+ h_temp)
    cv.rectangle(img_copy, location, bottom_right, (0,255,0), 2)
    cv.imshow('Matched template', img_copy)
    cv.waitKey(0)
    cv.destroyAllWindows()

quit()