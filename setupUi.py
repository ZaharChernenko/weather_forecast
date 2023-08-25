from PyQt5.QtGui import QFont


def setupRegularFont(font_size):
    regular_font = QFont()
    regular_font.setPointSize(font_size)
    return regular_font
