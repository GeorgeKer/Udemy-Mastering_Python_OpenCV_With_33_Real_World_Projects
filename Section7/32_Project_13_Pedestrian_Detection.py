import cv2 as cv
import imutils
import os

video_path = os.path.expanduser('~/INPUT/TEST_VIDEO.mp4')

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

cap = cv.VideoCapture(video_path)
while cap.isOpened():
    ret, img = cap.read()

    if ret:
        img = imutils.resize(image=img, width= int(img.shape[1]/2), height= int(img.shape[0]/2))
        
        (rects, weights) = hog.detectMultiScale(img, winStride=(4,4), padding=(4,4), scale=1.05)
        for (x, y, w, h) in rects:
            # if weights is not None and weights[0] < 0.8:
            #     continue
            # if w > h:
            #     cv.rectangle(img, (x,y), (x+w, y+w), (0,255,0), 1)
            # else:
            #     cv.rectangle(img, (x,y), (x+h, y+h), (0,255,0), 1)
            cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)

        cv.imshow('Pedestrian Detection', img)
        key = cv.waitKey(30)
        if key == 27:  # ESC key to exit
            break
    else:
        print('No frame to read')
        break

cap.release()
cv.destroyAllWindows()