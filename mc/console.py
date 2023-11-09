import click
import logging
import os
from mc import operations


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


@click.group()
@click.version_option(version="1.0.0")
def mc():
    """auto mc"""
    pass


@mc.command
def dig_stone():
    operations.dig_stone()


@mc.group()
def chest():
    pass


@chest.command
def store():
    operations.chest_store()


@chest.command
def restore():
    operations.chest_restore()


@mc.group()
def system():
    pass


@system.command()
@click.option("--key")
@click.option("--duration", type=int)
def hold(key: str, duration: int):
    if key.startswith("r"):
        operations.hold("right", duration)
    else:
        operations.hold("left", duration)


@mc.command()
@click.argument("steps", type=int)
def go_up(steps):
    operations.go_up(steps)


@mc.command()
@click.argument("row", type=int)
def transaction(row):
    operations.transaction(row)


@system.command()
def screenshot():
    operations.screen_shot()
