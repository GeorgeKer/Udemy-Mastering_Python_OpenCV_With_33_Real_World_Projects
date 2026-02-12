import cv2 as cv
import numpy as np
import os

def emptyFunction(x):
    pass

image = np.zeros((300, 500, 3), np.uint8)
cv.imshow("Color Palette", image)
windowTitle = "Color Palette"
cv.createTrackbar("Blue", windowTitle, 90, 255, emptyFunction)
cv.createTrackbar("Green", windowTitle, 60, 255, emptyFunction)
cv.createTrackbar("Red", windowTitle, 30, 255, emptyFunction)    

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    blue = cv.getTrackbarPos("Blue", windowTitle)
    green = cv.getTrackbarPos("Green", windowTitle)
    red = cv.getTrackbarPos("Red", windowTitle)
    
    image[:, 100:400] = [blue, green, red]

    cv.imshow(windowTitle, image)


cv.waitKey(0)
cv.destroyAllWindows()
quit()
