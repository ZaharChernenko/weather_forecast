from PyQt5.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QSize, Qt, QPropertyAnimation, pyqtProperty, QEasingCurve
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QColor, QPalette
from setupUi import setupRegularFont


class WeatherFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(200, 79))
        self.setMaximumSize(QSize(200, 79))

        regular_font = setupRegularFont(14)
        self.setFont(regular_font)
        self.setObjectName("button_frame")
        self.setStyleSheet("#button_frame{border-bottom: 1px solid rgba(255, 255, 255, 0.5);}")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.main_vlayout = QVBoxLayout(self)
        self.main_vlayout.setContentsMargins(7, 0, 7, 0)
        self.main_vlayout.setSpacing(0)

        self.main_btn_frame = QFrame(self)
        self.main_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.main_btn_frame.setFrameShadow(QFrame.Raised)
        self.main_btn_frame.setObjectName("main_btn_frame")
        self.main_btn_frame_hlayout = QHBoxLayout(self.main_btn_frame)
        self.main_btn_frame_hlayout.setContentsMargins(0, 0, 0, 0)
        self.main_btn_frame_hlayout.setSpacing(0)

        self.city_time_frame = QFrame(self.main_btn_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_time_frame.sizePolicy().hasHeightForWidth())
        self.city_time_frame.setSizePolicy(sizePolicy)
        self.city_time_frame.setMinimumSize(QSize(0, 44))
        self.city_time_frame.setFrameShape(QFrame.StyledPanel)
        self.city_time_frame.setFrameShadow(QFrame.Raised)
        self.city_time_frame.setObjectName("city_time_frame")
        self.city_time_vlayout = QVBoxLayout(self.city_time_frame)
        self.city_time_vlayout.setContentsMargins(0, 0, 0, 0)
        self.city_time_vlayout.setSpacing(0)
        self.city_time_vlayout.setObjectName("city_time_vlayout")

        self.city_btn = QPushButton(self.city_time_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_btn.sizePolicy().hasHeightForWidth())
        self.city_btn.setSizePolicy(sizePolicy)
        self.city_btn.setMinimumSize(QSize(146, 30))
        self.city_btn.setMaximumSize(QSize(146, 30))
        self.city_btn.setFont(regular_font)
        self.city_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.city_btn.setStyleSheet("text-align: left;")
        self.city_btn.setAutoDefault(False)
        self.city_btn.setDefault(False)
        self.city_btn.setFlat(False)
        self.city_btn.setObjectName("city_btn")
        self.city_time_vlayout.addWidget(self.city_btn)

        self.time_btn = QPushButton(self.city_time_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_btn.sizePolicy().hasHeightForWidth())
        self.time_btn.setSizePolicy(sizePolicy)
        self.time_btn.setMinimumSize(QSize(146, 14))
        self.time_btn.setMaximumSize(QSize(146, 14))
        regular_font.setPointSize(9)
        self.time_btn.setFont(regular_font)
        self.time_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.time_btn.setStyleSheet("text-align: left;")
        self.time_btn.setObjectName("time_btn")
        self.city_time_vlayout.addWidget(self.time_btn)
        self.main_btn_frame_hlayout.addWidget(self.city_time_frame)

        self.temp_btn = QPushButton(self.main_btn_frame)
        self.temp_btn.setMinimumSize(QSize(0, 51))
        self.temp_btn.setMaximumSize(QSize(16777215, 51))
        regular_font.setPointSize(26)
        self.temp_btn.setFont(regular_font)
        self.temp_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.temp_btn.setObjectName("temp_btn")
        self.main_btn_frame_hlayout.addWidget(self.temp_btn, 0, Qt.AlignRight)
        self.main_vlayout.addWidget(self.main_btn_frame)

        self.weather_btn = QPushButton(self)
        self.weather_btn.setMinimumSize(QSize(0, 35))
        self.weather_btn.setMaximumSize(QSize(16777215, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_btn.sizePolicy().hasHeightForWidth())
        self.weather_btn.setSizePolicy(sizePolicy)
        regular_font.setPointSize(11)
        self.weather_btn.setFont(regular_font)
        self.weather_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.weather_btn.setStyleSheet("text-align: right;")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/10d@2x.png"), QIcon.Normal, QIcon.Off)
        self.weather_btn.setIcon(icon)
        self.weather_btn.setIconSize(QSize(36, 36))
        self.weather_btn.setObjectName("weather_btn")
        self.main_vlayout.addWidget(self.weather_btn)

        self.city_btn.setText("Владивосток")
        self.time_btn.setText("00:00")
        self.temp_btn.setText("22°")
        self.weather_btn.setText("Макс: 28° | Мин: 22°")

        self.current_background_color = QPalette.Window
        self.background_anim = QPropertyAnimation(self, b"background")
        self.background_anim.setStartValue(QColor(255, 255, 255, 0))
        self.background_anim.setEndValue(QColor(255, 255, 255, 128))
        self.background_anim.setDuration(200)
        self.background_anim.setEasingCurve(QEasingCurve.InQuad)

    def parseStyleSheet(self):
        style_sheet_string = self.styleSheet()
        style_sheet_list = [s.strip() for s in style_sheet_string.split(';')]
        return style_sheet_list

    def getBackColor(self):
        return self.palette().color(self.current_background_color)

    def setBackColor(self, color):
        style_sheet_list = self.parseStyleSheet()
        bg_new = 'background-color: rgba(%d,%d,%d,%d)' % (color.red(), color.green(), color.blue(), color.alpha())

        for i, string in enumerate(style_sheet_list):
            if 'background-color' in string:
                style_sheet_list[i] = bg_new
                break
        else:
            style_sheet_list.insert(-1, bg_new)

        self.setStyleSheet('; '.join(style_sheet_list))

    background = pyqtProperty(QColor, getBackColor, setBackColor)

    def changeBorderToActive(self):
        style_sheet_list = self.parseStyleSheet()
        for i, string in enumerate(style_sheet_list):
            if "border-bottom" in string:
                style_sheet_list[i] = "#button_frame{border-radius: 10px;"
        self.setStyleSheet('; '.join(style_sheet_list))

    def animButton(self):
        self.background_anim.start()
        self.changeBorderToActive()
