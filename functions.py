"""
    Print a heading with customizable borders and width.

    Parameters:
        info (str): The heading text to display.
        border_char (str): The character used for the border (default: '-').
        width (int): The width of the border line (default: 30).
    """
def heading(info, border_char='-', width=30):
    border_line = border_char * width
    print(border_line)
    print(info.center(width))
    print(border_line)