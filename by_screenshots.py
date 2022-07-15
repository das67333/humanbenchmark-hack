# ~20 ms

import numpy as np
import time
import pyautogui
import PIL.Image
import mss

pos = (1440, 540)
mouse_pointer_shift = 20

clicks = 5
with mss.mss() as sct:
    m = sct.monitors[1]
    box = (m['left'] + pos[0] + mouse_pointer_shift, m['top'] + pos[1],
           m['left'] + pos[0] + 1 + mouse_pointer_shift, m['top'] + pos[1] + 1)

    while clicks:
        sct_img = sct.grab(box)
        r, g, b = PIL.Image.frombytes(
            "RGB", sct_img.size, sct_img.rgb).load()[0, 0]
        if g / (b + 1) > 1.2 and g / (r + 1) > 1.5:
            pyautogui.click(x=pos[0], y=pos[1])
            time.sleep(0.5)
            pyautogui.click(x=pos[0], y=pos[1])
            time.sleep(0.5)
            clicks -= 1
