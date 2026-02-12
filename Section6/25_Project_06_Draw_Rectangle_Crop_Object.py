import cv2 as cv
import numpy as np
import argparse
import os

img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img = cv.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

ref_points = []
cropping = False

def img_selection(event, x, y, flags, param):
    global ref_points, cropping
    
    if event == cv.EVENT_LBUTTONDOWN:
        ref_points = [(x, y)]
    elif event == cv.EVENT_LBUTTONUP:
        ref_points.append((x, y))
        cropping = True
        
        cv.rectangle(img, ref_points[0], ref_points[1], (0, 255, 0), 3)
        cv.imshow("Image", img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw rectangles to extract objects from an image.')
    parser.add_argument('--input_image', type=str, default=img_path)
    parser.add_argument('--output_dir', type=str, default=os.path.expanduser('~/OUTPUT/OPENCV_TEST/'))
    args = parser.parse_args()

    clone = img.copy()
    cv.namedWindow("Image to Crop")
    cv.setMouseCallback("Image to Crop", img_selection)

    while True:
        cv.imshow("Image to Crop", img)
        key = cv.waitKey(1) & 0xFF
        
        if key == ord("r"):
            img = clone.copy()
        elif key == ord("c"):
            break
    
    if len(ref_points) == 2:
        cropped_img = clone[ref_points[0][1]:ref_points[1][1], ref_points[0][0]:ref_points[1][0]]
        cv.imshow("Cropped Image", cropped_img)
        cv.waitKey(0)
    
    cv.destroyAllWindows()
    quit()