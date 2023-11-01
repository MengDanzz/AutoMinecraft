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


def get_command_tree(command):
    if isinstance(command, click.Group):
        command_dict = {"name": command.name, "help": command.help, "subcommands": {}}
        # flake8 noqa
        for subcommand_name, subcommand in command.commands.items():
            command_dict["subcommands"][subcommand_name] = get_command_tree(subcommand)
        return command_dict
    elif isinstance(command, click.Command):
        return {"name": command.name, "help": command.help}


@mc.command
@click.argument("prev", required=False)
@click.argument("cur", required=False)
def autocomp(prev: str, cur: str):
    # auto complete
    cmd_tree = get_command_tree(mc)
    prevs = prev.strip().split(" ")[1:]  # first item is mc
    cmd_cursor = cmd_tree

    for cmd in prevs:
        cmd_cursor = cmd_cursor["subcommands"][cmd]
    if "subcommands" in cmd_cursor:
        click.echo("\n".join([cmd for cmd in cmd_cursor["subcommands"]]))
    else:
        pass


if __name__ == "__main__":
    print("aumc")
