import cv2 as cv
import imutils
from imutils.object_detection import non_max_suppression
import os
import numpy as np

video_path = os.path.expanduser('~/INPUT/TEST_VIDEO.mp4')

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

cap = cv.VideoCapture(video_path)
while cap.isOpened():
    ret, img = cap.read()

    if ret:
        img = imutils.resize(image=img, width= int(img.shape[1]/2), height= int(img.shape[0]/2))
        
        (rects, weights) = hog.detectMultiScale(img, winStride=(4,4), padding=(8,8), scale=1.25)
        # for (x, y, w, h) in rects:
            # cv.rectangle(img, (x,y), (x+w, y+h), (0,0, 255), 1)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv.rectangle(img, (xA, yA), (xB, yB), (0,255,0), 1)
        
        cv.imshow('Pedestrian Detection', img)
        key = cv.waitKey(30) 
        if key == 27:  # ESC key to exit
            break
    else:
        print('No frame to read')
        break

cap.release()
cv.destroyAllWindows()