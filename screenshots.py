# ~20 ms

import numpy as np
import time
import pyautogui
import PIL.Image
import mss


clicks = 5
with mss.mss() as sct:
    m = sct.monitors[1]
    box = (m['left'] + 1460, m['top'] + 540, m['left'] + 1461, m['top'] + 541)

    while clicks:
        sct_img = sct.grab(box)
        r, g, b = PIL.Image.frombytes("RGB", sct_img.size, sct_img.rgb).load()[0, 0]
        if g / (b + 1) > 1.2 and g / (r + 1) > 1.5:
            pyautogui.click(x=1440, y=540)
            time.sleep(0.5)
            pyautogui.click(x=1440, y=540)
            time.sleep(0.5)
            clicks -= 1


# while clicks:

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     b, g, r = np.mean(frame[240, :], axis=0)
#     if g / (b + 1) > 1.2 and g / (r + 1) > 1.5:
#         pyautogui.click(x=1440, y=540)
#         time.sleep(0.5)
#         pyautogui.click(x=1440, y=540)
#         time.sleep(0.5)
#         clicks -= 1
