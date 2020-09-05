import sys

if sys.platform == "win32" and sys.stdin.isatty():
    FOREGROUND_BLACK = 0x00  # black.
    FOREGROUND_DARKBLUE = 0x01  # dark blue.
    FOREGROUND_DARKGREEN = 0x02  # dark green.
    FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
    FOREGROUND_DARKRED = 0x04  # dark red.
    FOREGROUND_DARKPINK = 0x05  # dark pink.
    FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
    FOREGROUND_DARKWHITE = 0x07  # dark white.
    FOREGROUND_DARKGRAY = 0x08  # dark gray.
    FOREGROUND_BLUE = 0x09  # blue.
    FOREGROUND_GREEN = 0x0a  # green.
    FOREGROUND_SKYBLUE = 0x0b  # skyblue.
    FOREGROUND_RED = 0x0c  # red.
    FOREGROUND_PINK = 0x0d  # pink.
    FOREGROUND_YELLOW = 0x0e  # yellow.
    FOREGROUND_WHITE = 0x0f  # white.
    FOREGROUND_PURPLE = FOREGROUND_PINK
    FOREGROUND_CYAN = FOREGROUND_PINK

    BACKGROUND_BLACK = 0x00
    BACKGROUND_DARKBLUE = 0x10  # dark blue.
    BACKGROUND_DARKGREEN = 0x20  # dark green.
    BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
    BACKGROUND_DARKRED = 0x40  # dark red.
    BACKGROUND_DARKPINK = 0x50  # dark pink.
    BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
    BACKGROUND_DARKWHITE = 0x70  # dark white.
    BACKGROUND_DARKGRAY = 0x80  # dark gray.
    BACKGROUND_BLUE = 0x90  # blue.
    BACKGROUND_GREEN = 0xa0  # green.
    BACKGROUND_SKYBLUE = 0xb0  # skyblue.
    BACKGROUND_RED = 0xc0  # red.
    BACKGROUND_PINK = 0xd0  # pink.
    BACKGROUND_YELLOW = 0xe0  # yellow.
    BACKGROUND_WHITE = 0xf0  # white.
    BACKGROUND_PURPLE = BACKGROUND_PINK
    BACKGROUND_CYAN = BACKGROUND_PINK
else:
    FOREGROUND_BLACK = 30
    FOREGROUND_RED = 31
    FOREGROUND_GREEN = 32
    FOREGROUND_YELLOW = 33
    FOREGROUND_BLUE = 34
    FOREGROUND_PURPLE = 35
    FOREGROUND_CYAN = 36
    FOREGROUND_WHITE = 37
    FOREGROUND_SKYBLUE = FOREGROUND_BLUE
    FOREGROUND_PINK = FOREGROUND_PURPLE
    FOREGROUND_DARKBLUE = FOREGROUND_BLUE
    FOREGROUND_DARKGREEN = FOREGROUND_GREEN
    FOREGROUND_DARKSKYBLUE = FOREGROUND_BLUE
    FOREGROUND_DARKRED = FOREGROUND_RED
    FOREGROUND_DARKPINK = FOREGROUND_CYAN
    FOREGROUND_DARKYELLOW = FOREGROUND_YELLOW
    FOREGROUND_DARKWHITE = FOREGROUND_WHITE
    FOREGROUND_DARKGRAY = FOREGROUND_BLACK

    BACKGROUND_BLACK = 40
    BACKGROUND_RED = 41
    BACKGROUND_GREEN = 42
    BACKGROUND_YELLOW = 43
    BACKGROUND_BLUE = 44
    BACKGROUND_PURPLE = 45
    BACKGROUND_CYAN = 46
    BACKGROUND_WHITE = 47
    BACKGROUND_SKYBLUE = BACKGROUND_BLUE
    BACKGROUND_PINK = BACKGROUND_PURPLE
    BACKGROUND_DARKBLUE = BACKGROUND_BLUE
    BACKGROUND_DARKGREEN = BACKGROUND_GREEN
    BACKGROUND_DARKSKYBLUE = BACKGROUND_BLUE
    BACKGROUND_DARKRED = BACKGROUND_RED
    BACKGROUND_DARKPINK = BACKGROUND_PURPLE
    BACKGROUND_DARKYELLOW = BACKGROUND_YELLOW
    BACKGROUND_DARKWHITE = BACKGROUND_WHITE
    BACKGROUND_DARKGRAY = BACKGROUND_BLACK
    
MODE_NORMAL = 0
MODE_BOLD = 1
MODE_UNDERLINE = 4
MODE_BLINK = 5
MODE_INVERT = 7
MODE_HIDE = 8
