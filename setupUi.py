from PyQt5.QtWidgets import QPushButton, QSizePolicy, QGraphicsColorizeEffect, QCompleter
from PyQt5.QtCore import QSize, Qt, QPropertyAnimation, QEvent, QEasingCurve
from PyQt5.QtGui import QFont, QCursor, QIcon, QPixmap, QColor


def setupRegularFont(font_size):
    regular_font = QFont()
    regular_font.setPointSize(font_size)
    return regular_font


def setupQCompleter(arr):
    completer = QCompleter(arr)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    completer.popup().setObjectName("completerPopup")
    completer.setMaxVisibleItems(15)
    completer.popup().setStyleSheet("color: white; background: transparent; border-radius: 5px; font-size: 14px;")
    return completer


class CustomButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
        self.setCursor(QCursor(Qt.PointingHandCursor))

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/slider_icon.svg"), QIcon.Normal, QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QSize(45, 45))

        self.color_effect = QGraphicsColorizeEffect()
        self.color_effect.setColor(QColor(255, 255, 255, 128))
        self.setGraphicsEffect(self.color_effect)

        self.icon_anim = QPropertyAnimation(self.color_effect, b"color")
        self.icon_anim.setStartValue(QColor(255, 255, 255, 128))
        self.icon_anim.setEndValue(QColor(255, 255, 255, 255))
        self.icon_anim.setDuration(450)
        self.icon_anim.setEasingCurve(QEasingCurve.InQuad)

    def enterEvent(self, a0: QEvent):
        self.icon_anim.setDirection(self.icon_anim.Forward)
        self.icon_anim.start()

    def leaveEvent(self, a0: QEvent):
        self.icon_anim.setDirection(self.icon_anim.Backward)
        self.icon_anim.start()
