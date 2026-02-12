import cv2 as cv
import os 

video_path = os.path.expanduser("~/INPUT/P1020601.mp4")

def rescale_frame(frame, scale=0.5):
    new_width = int(frame.shape[1] * scale)
    new_height = int(frame.shape[0] * scale)
    
    return cv.resize(frame, (new_width, new_height), interpolation=cv.INTER_AREA)
    

videoCap = cv.VideoCapture(video_path)

while True:
    exists, frame = videoCap.read()
    scaled_frame = rescale_frame(frame)
    cv.imshow('scale test', scaled_frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

videoCap.release()
cv.destroyAllWindows()

quit()