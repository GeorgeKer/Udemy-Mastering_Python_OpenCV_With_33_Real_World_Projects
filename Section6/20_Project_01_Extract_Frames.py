import cv2 as cv
import numpy as np
import os

input_video_path = os.path.expanduser('~/INPUT/P1020609.mp4')

def extract_frames(video_path):
    cap = cv.VideoCapture(video_path)

    count = 0
    success = True
    while success:
        success, frame = cap.read()
        if success and count % 2 == 0:
            frame_filename = os.path.expanduser(f'~/OUTPUT/OPENCV_TEST/frame_{count:04d}.jpg')
            cv.imwrite(frame_filename, frame)
        count += 1

    cap.release()
    
if __name__ == "__main__":
    extract_frames(input_video_path)
    quit()