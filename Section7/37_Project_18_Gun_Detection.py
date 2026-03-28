import cv2 as cv
import os
import imutils

gun_cascade = cv.CascadeClassifier('gun_cascade.xml')
video_input = cv.VideoCapture(0)

first_frame = None
gun_detected = False

while True:
    ret, frame = video_input.read()
    frame = imutils.resize(frame, width=500)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(guns) > 0:
        gun_detected = True
        for (x, y, w, h) in guns:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, 'Gun Detected', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    else:
        gun_detected = False
    
    cv.imshow('Gun Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_input.release()
cv.destroyAllWindows()