import cv2 as cv
import numpy as np
import os

cap = cv.VideoCapture(0)
FourCC = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter('output.avi', FourCC, 24.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv.imshow('Video Feed', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
quit()