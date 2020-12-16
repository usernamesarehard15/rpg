def colorStr(string, col):
    """Returns a coloured version of the input string

    Keyword arguments:
    string -- input string
    col -- tuple of 3 ints from 0-5, representing the text colour
    """
    if 1 >= col[0] >= 5 or 1 >= col[1] >= 5 or 1 >= col[2] >= 5:
        return
    col = str(col[0] * 36 + col[1] * 6 + col[2] + 16)
    return f'\u001b[38;5;{col}m{string}\u001b[0m'


def colorStrBkr(string, col):
    """Returns the input string with a background colour

    Keyword arguments:
    string -- input string
    col -- tuple of 3 ints from 0-5, representing the background colour
    """
    if 1 >= col[0] >= 5 or 1 >= col[1] >= 5 or 1 >= col[2] >= 5:
        return
    col = str(col[0] * 36 + col[1] * 6 + col[2] + 16)
    return f'\u001b[48;5;{col}m{string}\u001b[0m'
