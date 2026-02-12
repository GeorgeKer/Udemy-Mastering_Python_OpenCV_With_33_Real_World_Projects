import cv2 as cv
import numpy as np
import os

video_path = os.path.expanduser('~/INPUT/P1020609.mp4')
cap = cv.VideoCapture(video_path)

check, frame = cap.read()
counter = 0
frame_list = []

while check:
    frame_list.append(frame)
    cv.imwrite(f'~/OUTPUT/frame_{counter:04d}.png', frame)

    counter += 1
    check, frame = cap.read()

frame_list.reverse()

for i, frame in enumerate(frame_list):
    cv.imshow('Inverse Video Playing', frame)

    key = cv.waitKey(30)
    if key == 27:  # ESC key to exit
        break

cap.release()
cv.destroyAllWindows()
quit()