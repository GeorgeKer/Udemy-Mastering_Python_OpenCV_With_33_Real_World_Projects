import cv2 as cv
import numpy as np
import os

INPUT_VIDEO = os.path.expanduser('~/INPUT/TEST_VIDEO_people.mp4')
HAARCASCADE_FRONTALFACE_XML = 'haarcascade_frontalface_default.xml'

face_cascade = cv.CascadeClassifier(HAARCASCADE_FRONTALFACE_XML)
video_cap = cv.VideoCapture(INPUT_VIDEO)

while video_cap.isOpened():
    ret, frame = video_cap.read()
    if not ret: break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv.imshow('Face Detection', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv.destroyAllWindows()