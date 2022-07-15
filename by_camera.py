# ~90 ms

import cv2
import numpy as np
import time
import pyautogui

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not (cap.isOpened()):
    print('Could not open video device')

# 480*640, 30 fps
clicks = 5
while clicks:
    frame = cap.read()[1]
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    b, g, r = np.mean(frame[240, :], axis=0)
    if g / (b + 1) > 1.2 and g / (r + 1) > 1.5:
        pyautogui.click(x=1440, y=540)
        time.sleep(0.5)
        pyautogui.click(x=1440, y=540)
        time.sleep(0.5)
        cap.read()
        clicks -= 1

cap.release()
