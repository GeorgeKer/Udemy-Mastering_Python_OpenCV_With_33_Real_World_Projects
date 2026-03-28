import cv2 as cv
import os

VIDEO_PATH = os.path.expanduser('~/INPUT/TEST_VIDEO_cars.mp4')
cars_cascade = cv.CascadeClassifier('../cars_cascade.xml')
video_cap = cv.VideoCapture('cars.mp4')

while True:
    ret, frame = video_cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cars = cars_cascade.detectMultiScale(gray, 1.1, 1)
    if len(cars) > 0:
        for (x, y, w, h) in cars:
            cv.rectangle(img=frame, (x,y), (x+w, y+h), (255, 255, 255), 1) # type: ignore

    cv.imshow('Car Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv.destroyAllWindows()