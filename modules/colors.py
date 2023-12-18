from colorama import Fore, Back, Style

def colors(string, color, back=False):
    """Make things colorful

    Arguments:
        string {str} -- String to apply colors on
        color {str} -- value of color to apply

    """
    if back:
        return f"{Back.__dict__[color.upper()]}{string}{Style.RESET_ALL}"
    color_dict = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'reset': Fore.RESET
    }

    return f"{color_dict[color]}{string}{Style.RESET_ALL}"