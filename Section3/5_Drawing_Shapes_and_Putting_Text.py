import cv2 as cv
import numpy as np

img_canvas = np.zeros((1920//2,1080//2, 3), dtype=np.uint8)

# img[100:200, 300:400] = 255, 0, 0
cv.rectangle(img_canvas, (100, 50), (150,200), (100, 100, 200), thickness=5)
cv.circle(
    img_canvas,
    (img_canvas.shape[1]//2, img_canvas.shape[0]//2), 40,
    color=(200, 200, 100),
    thickness=cv.FILLED
    )
cv.line(img_canvas, (100,0), (img_canvas.shape[1]//2, img_canvas.shape[0]//2), (255,255,255), thickness=1)
cv.putText(
    img_canvas,
    'Hello OpenCV',
    org=(0, 300),
    fontFace=cv.FONT_HERSHEY_SIMPLEX,
    fontScale=.5,
    color=(150, 150, 150),
    thickness=1
    )

cv.imshow('Test!', img_canvas)

cv.waitKey(0)
quit()
