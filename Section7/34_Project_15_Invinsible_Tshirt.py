import cv2 as cv
import numpy as np
import time

capture_video = cv.VideoCapture(0)

time.sleep(2)
background = 0

for i in range(60):
    ret, background = capture_video.read()
    if not ret: continue
    
while capture_video.isOpened():
    ret, img = capture_video.read()
    if not ret: break
    
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    lower_red_mask = np.array([100, 40, 40])
    higher_red_mask = np.array([100, 255, 255])
    mask1 = cv.inRange(hsv, lower_red_mask, higher_red_mask)
    
    lower_red_mask = np.array([150, 40, 40])
    higher_red_mask = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv, lower_red_mask, higher_red_mask)
    
    mask = mask1 + mask2
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2) # type: ignore
    mask = cv.dilate(mask, np.ones((3, 3), np.uint8), iterations=1) # type: ignore

    mask_inverse = cv.bitwise_not(mask)
    
    res1 = cv.bitwise_and(background, background, mask=mask_inverse) # type: ignore
    res2 = cv.bitwise_and(img, img, mask=mask) # type: ignore

    output = cv.addWeighted(res1, 1, res2, 1, 0)

    cv.imshow("Invisible RED mask", output)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture_video.release()
cv.destroyAllWindows()
