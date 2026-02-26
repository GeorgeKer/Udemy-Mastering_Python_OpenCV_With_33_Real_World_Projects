import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

video_path = os.path.expanduser('~/INPUT/TEST_VIDEO.mp4')
cap = cv.VideoCapture(video_path)

while True:
    check, frame = cap.read()
    if not check:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 170])
    upper_red = np.array([10, 255, 255])
    mask1 = cv.inRange(hsv, lower_red, upper_red)

    # lower_red = np.array([170, 120, 70])
    # upper_red = np.array([180, 255, 255])
    # mask2 = cv.inRange(hsv, lower_red, upper_red)

    mask = mask1 #+ mask2

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Original Video', frame)
    cv.imshow('Red Color Detection', result)

    key = cv.waitKey(30)
    if key == 27:  # ESC key to exit
        break