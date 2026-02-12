import os
# from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows
import cv2

video_path = os.path.expanduser("~/INPUT/P1020601.mp4")

videoCap = cv2.VideoCapture(video_path)
while True:
    isTrue, frame = videoCap.read()
    cv2.imshow('video_window', frame)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

videoCap.release()
cv2.destroyAllWindows()