import os
import pyautogui
from time import sleep


def focus():
    os.system(
        # flake8: noqa: E501
        'bash -c "xdotool windowactivate $(xdotool search --class Minecraft); "'
    )
    pyautogui.moveTo(960, 532)  # For 1920*1080

    pyautogui.press("esc")
    sleep(1)
