import cv2 as cv
import os

for e in dir(cv):
    if "EVENT" in e:
        print(e)

# img_path = os.path.expanduser('~/INPUT/TEST_IMAGE.jpg')
img_path = os.path.expanduser('~/INPUT/vlcsnap-2025-12-27-21h17m25s629.png')
img = cv.imread(img_path, 1)
cv.imshow('Image', img)

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"X={x}, Y={y}")
        print(f"{x}, {y}")

        print(img[y, x])  # BGR format
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(f"Red={red}, Green={green}, Blue={blue}")
    
if __name__ == "__main__":
    print("Click on the image to get the coordinates of the mouse click.")
    cv.setMouseCallback('Image', click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()
    quit()
