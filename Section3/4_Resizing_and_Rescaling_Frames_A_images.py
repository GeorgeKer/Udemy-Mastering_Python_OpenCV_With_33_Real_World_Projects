import cv2 as cv
import os 

image_path = os.path.expanduser("~/INPUT/TEST_IMAGE.jpg")

def rescale_frame(frame, scale=0.6):
    new_width = int(frame.shape[1] * scale)
    new_height = int(frame.shape[0] * scale)
    
    return cv.resize(frame, (new_width, new_height), interpolation=cv.INTER_AREA)
    
image = cv.imread(image_path)
scaled_image = rescale_frame(image)

cv.imshow('scale test', scaled_image)
cv.waitKey(0)
cv.destroyAllWindows()
quit()