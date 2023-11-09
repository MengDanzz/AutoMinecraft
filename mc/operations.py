import datetime
import logging
import os.path
from typing import Tuple
from mc import window
import functools
import pyautogui
from time import sleep
from itertools import product


def mc_executor(func):
    """
    Every command need to enter game first
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        window.focus()
        return func(*args, **kwargs)

    return wrapper


@mc_executor
def dig_stone():
    for i in range(9):
        # pyautogui.moveTo(0, 0, duration=0.5)
        pyautogui.mouseDown()
        sleep(200)
        pyautogui.mouseUp()
        pyautogui.scroll(-1)


@mc_executor
def transaction(row: int):
    X = 605
    FIRST_Y = 293
    ROW_HEIGHT = 78.67

    pyautogui.rightClick()
    if row > 7:
        pyautogui.scroll(-2)
        row = row - 2

    with pyautogui.hold("shift"):
        for i in range(15):
            pyautogui.click(X, FIRST_Y + (row - 1) * ROW_HEIGHT)
            pyautogui.click(1308, 367)


CHEST_ROWS = 3
CHEST_COLS = 9
PACK_ROWS = 3
PACK_COLS = 9


def get_pos_in_chest(x, y) -> Tuple[int, int]:
    POS0_X, POS0_Y = 671, 274
    WIDTH, HEIGHT = 72.37, 88.5
    return int(POS0_X + x * WIDTH), int(POS0_Y + y * HEIGHT)


def get_pos_in_pack(x, y) -> Tuple[int, int]:
    POS0_X, POS0_Y = 674, 541
    WIDTH, HEIGHT = 72.37, 88.5
    return int(POS0_X + x * WIDTH), int(POS0_Y + y * HEIGHT)


@mc_executor
def chest_store():
    pyautogui.rightClick()
    with pyautogui.hold("shift"):
        for x, y in product(range(PACK_COLS), range(PACK_ROWS)):
            pyautogui.click(*get_pos_in_pack(x, y))


@mc_executor
def go_up(steps: int):
    with pyautogui.hold("space"):
        for _ in range(steps):
            pyautogui.click(button="right")
            sleep(0.35)
            pyautogui.keyDown("space")


@mc_executor
def hold(key: str, duration):
    pyautogui.mouseDown(button=key)
    sleep(duration)
    pyautogui.mouseUp(button=key)


@mc_executor
def chest_restore():
    pyautogui.rightClick()
    with pyautogui.hold("shift"):
        for x, y in product(range(PACK_COLS), range(PACK_ROWS)):
            pyautogui.click(*get_pos_in_chest(x, y))


@mc_executor
def screen_shot():
    img = pyautogui.screenshot()
    save_path = os.path.join("/tmp/", str(datetime.datetime.now().timestamp()) + ".png")
    img.save(save_path)
    logging.info(f"save to {save_path}")
