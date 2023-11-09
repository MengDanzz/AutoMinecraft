import os
import sys

import pyautogui
from time import sleep
import keyboard


def focus():
    os.system(
        # flake8: noqa: E501
        'bash -c "xdotool windowactivate $(xdotool search --class Minecraft); "'
    )
    #    keyboard.add_hotkey("ctrl+esc+m",sys.exit)
    pyautogui.moveTo(960, 532)  # For 1920*1080

    pyautogui.press("esc")
    sleep(1)
