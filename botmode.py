import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui

# Grab a certain region of the screen
def grab_screen(region=None):
    img = ImageGrab.grab(bbox=region)
    return img

while True:
    # Capture game screen of interest and convert it to a np array
    frame = np.array(grab_screen((800, 400, 1200, 600)))
    danger = np.array(grab_screen((1014, 500, 1020, 501)))

    # Convert RGB -> BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    danger = cv2.cvtColor(danger, cv2.COLOR_RGB2BGR)
    
    for x in danger[0]:
        if x[0] == 83:
            print("Danger")
            pyautogui.press('space')
            print("Jump")

    cv2.imshow('frame', danger)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
