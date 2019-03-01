from os import system

COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
}


def print_color(msg, color):
    color = COLORS.get(color, str(color))
    system(f"echo [{color}m{msg}[0m")


print_color("wow", "red")
print_color("this", "green")
print_color("is", "blue")
print_color("so", "magenta")
print_color("cool", "cyan")
