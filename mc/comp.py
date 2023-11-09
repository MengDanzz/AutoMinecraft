from mc.console import mc
import click
import sys


def get_command_tree(command):
    if isinstance(command, click.Group):
        command_dict = {"name": command.name, "help": command.help, "subcommands": {}}
        # flake8 noqa
        for subcommand_name, subcommand in command.commands.items():
            command_dict["subcommands"][subcommand_name] = get_command_tree(subcommand)
        return command_dict
    elif isinstance(command, click.Command):
        return {"name": command.name, "help": command.help, "options": command.params}


def autocomp():
    if len(sys.argv) < 2:
        return
    prev = sys.argv[1]
    # auto complete
    cmd_tree = get_command_tree(mc)
    prevs = prev.strip().split(" ")[1:]  # first item is mc
    cmd_cursor = cmd_tree

    for cmd in prevs:
        if "subcommands" not in cmd_cursor:  # may adding options
            break
        cmd_cursor = cmd_cursor["subcommands"][cmd]
    if "subcommands" in cmd_cursor:
        # has subcommands
        click.echo("\n".join([cmd for cmd in cmd_cursor["subcommands"]]))
    else:
        # command
        options = cmd_cursor["options"]
        prompts = []
        for opt in options:
            if not isinstance(opt, click.Option):
                continue
            if opt.type == bool:
                prompts.append(f"--{opt.name}")
            else:
                prompts.append(f"--{opt.name}==")
        click.echo("\n".join(prompts))
