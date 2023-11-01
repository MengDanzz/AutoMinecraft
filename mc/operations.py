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
def chest_restore():
    pyautogui.rightClick()
    with pyautogui.hold("shift"):
        for x, y in product(range(PACK_COLS), range(PACK_ROWS)):
            pyautogui.click(*get_pos_in_chest(x, y))
