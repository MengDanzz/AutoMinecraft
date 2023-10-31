import os


def focus():
    os.system(
        # flake8: noqa: E501
        'bash -c "xdotool windowactivate $(xdotool search --class Minecraft); xdotool key Escape;"'
    )
