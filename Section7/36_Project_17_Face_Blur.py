import cv2 as cv
import os

# INPUT_VIDEO = os.path.expanduser('~/INPUT/TEST_VIDEO_people.mp4')
INPUT_VIDEO = os.path.expanduser('~/INPUT/P1190820_2023528.MP4')
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

assert INPUT_VIDEO is not None
assert os.path.exists(INPUT_VIDEO)
assert face_cascade is not None
assert not face_cascade.empty()

video_cap = cv.VideoCapture(INPUT_VIDEO)

while True:
    ret, frame = video_cap.read()
    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)

    if not ret: break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=9)

    for (x, y , w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        face_blurred = cv.GaussianBlur(face_roi, (99, 99), 9)
        frame[y:y+h, x:x+w] = face_blurred
    
    cv.imshow('Blur that face!', frame)
    
    key = cv.waitKey(30)
    if key == 27:  # ESC key to exit
        break

video_cap.release()
cv.destroyAllWindows()