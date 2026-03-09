import cv2 as cv
import os

VIDEO_PATH = os.path.expanduser('~/INPUT/TEST_VIDEO_people.mp4')

fgbgMOG = cv.createBackgroundSubtractorMOG2()
fgbgKNN = cv.createBackgroundSubtractorKNN()

cap = cv.VideoCapture(VIDEO_PATH)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        fgmaskMOG = fgbgMOG.apply(frame)
        fgmaskKNN = fgbgKNN.apply(frame)

        cv.imshow('Frame', frame)
        cv.imshow('MOG', fgmaskMOG)
        cv.imshow('KNN', fgmaskKNN)

        key = cv.waitKey(30) 
        if key == 27:  # ESC key to exit
            break
    else:
        print('No frame to read')
        break

cap.release()
cv.destroyAllWindows()