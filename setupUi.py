from PyQt5.QtWidgets import QPushButton, QSizePolicy, QGraphicsColorizeEffect
from PyQt5.QtCore import QSize, Qt, QPropertyAnimation, QEvent, QEasingCurve, pyqtProperty
from PyQt5.QtGui import QFont, QCursor, QIcon, QPixmap, QColor, QPalette


def setupRegularFont(font_size):
    regular_font = QFont()
    regular_font.setPointSize(font_size)
    return regular_font


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
        self.setStyleSheet("border-radius: 5px;")

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
