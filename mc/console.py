import click
import logging
import os
import functools
from mc import window

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


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


@click.group()
@click.version_option(version="1.0.0")
def mc():
    """auto mc"""
    pass


@mc.command
@mc_executor
def dig_stone():
    print("hehehe")


if __name__ == "__main__":
    print("aumc")
