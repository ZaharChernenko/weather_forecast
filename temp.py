# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 670)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#slider{\n"
"    margin: 15 0 15 0;\n"
"    border-right: 1px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"#weather_line_edit{\n"
"    border-radius: 3px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_hlayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.main_hlayout.setContentsMargins(0, 0, 0, 0)
        self.main_hlayout.setSpacing(0)
        self.main_hlayout.setObjectName("main_hlayout")
        self.slider = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy)
        self.slider.setMinimumSize(QtCore.QSize(235, 0))
        self.slider.setMaximumSize(QtCore.QSize(235, 16777215))
        self.slider.setStyleSheet("")
        self.slider.setObjectName("slider")
        self.slider_vlayout = QtWidgets.QVBoxLayout(self.slider)
        self.slider_vlayout.setContentsMargins(0, 0, 0, 0)
        self.slider_vlayout.setSpacing(0)
        self.slider_vlayout.setObjectName("slider_vlayout")
        self.scroll_area = QtWidgets.QScrollArea(self.slider)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 235, 670))
        self.scroll_area_widget.setObjectName("scroll_area_widget")
        self.scroll_area_vlayout = QtWidgets.QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_vlayout.setContentsMargins(15, 15, 0, 0)
        self.scroll_area_vlayout.setSpacing(0)
        self.scroll_area_vlayout.setObjectName("scroll_area_vlayout")
        self.button_frame = QtWidgets.QFrame(self.scroll_area_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setMinimumSize(QtCore.QSize(205, 79))
        self.button_frame.setMaximumSize(QtCore.QSize(205, 79))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_frame.setFont(font)
        self.button_frame.setStyleSheet("#button_frame{\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgba(255, 255, 255, 0.5);\n"
"  border-radius: 10px;\n"
"}")
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.button_frame_vlayout = QtWidgets.QVBoxLayout(self.button_frame)
        self.button_frame_vlayout.setContentsMargins(7, 0, 7, 0)
        self.button_frame_vlayout.setSpacing(0)
        self.button_frame_vlayout.setObjectName("button_frame_vlayout")
        self.main_btn_frame = QtWidgets.QFrame(self.button_frame)
        self.main_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_btn_frame.setObjectName("main_btn_frame")
        self.main_btn_frame_hlayout = QtWidgets.QHBoxLayout(self.main_btn_frame)
        self.main_btn_frame_hlayout.setContentsMargins(0, 0, 0, 0)
        self.main_btn_frame_hlayout.setSpacing(0)
        self.main_btn_frame_hlayout.setObjectName("main_btn_frame_hlayout")
        self.city_time_frame = QtWidgets.QFrame(self.main_btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_time_frame.sizePolicy().hasHeightForWidth())
        self.city_time_frame.setSizePolicy(sizePolicy)
        self.city_time_frame.setMinimumSize(QtCore.QSize(0, 44))
        self.city_time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.city_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.city_time_frame.setObjectName("city_time_frame")
        self.city_time_vlayout = QtWidgets.QVBoxLayout(self.city_time_frame)
        self.city_time_vlayout.setContentsMargins(0, 0, 0, 0)
        self.city_time_vlayout.setSpacing(0)
        self.city_time_vlayout.setObjectName("city_time_vlayout")
        self.city_btn = QtWidgets.QPushButton(self.city_time_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_btn.sizePolicy().hasHeightForWidth())
        self.city_btn.setSizePolicy(sizePolicy)
        self.city_btn.setMinimumSize(QtCore.QSize(146, 30))
        self.city_btn.setMaximumSize(QtCore.QSize(146, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.city_btn.setFont(font)
        self.city_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.city_btn.setStyleSheet("text-align: left;")
        self.city_btn.setAutoDefault(False)
        self.city_btn.setDefault(False)
        self.city_btn.setFlat(False)
        self.city_btn.setObjectName("city_btn")
        self.city_time_vlayout.addWidget(self.city_btn)
        self.time_frame = QtWidgets.QFrame(self.city_time_frame)
        self.time_frame.setMinimumSize(QtCore.QSize(0, 14))
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time_frame.setObjectName("time_frame")
        self.time_hlayout = QtWidgets.QHBoxLayout(self.time_frame)
        self.time_hlayout.setContentsMargins(0, 0, 0, 0)
        self.time_hlayout.setSpacing(0)
        self.time_hlayout.setObjectName("time_hlayout")
        self.time_btn = QtWidgets.QPushButton(self.time_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_btn.sizePolicy().hasHeightForWidth())
        self.time_btn.setSizePolicy(sizePolicy)
        self.time_btn.setMinimumSize(QtCore.QSize(0, 14))
        self.time_btn.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.time_btn.setFont(font)
        self.time_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.time_btn.setStyleSheet("text-align: left;")
        self.time_btn.setObjectName("time_btn")
        self.time_hlayout.addWidget(self.time_btn)
        self.city_time_vlayout.addWidget(self.time_frame)
        self.main_btn_frame_hlayout.addWidget(self.city_time_frame)
        self.temp_btn = QtWidgets.QPushButton(self.main_btn_frame)
        self.temp_btn.setMinimumSize(QtCore.QSize(0, 51))
        self.temp_btn.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.temp_btn.setFont(font)
        self.temp_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.temp_btn.setObjectName("temp_btn")
        self.main_btn_frame_hlayout.addWidget(self.temp_btn, 0, QtCore.Qt.AlignRight)
        self.button_frame_vlayout.addWidget(self.main_btn_frame)
        self.weather_frame = QtWidgets.QFrame(self.button_frame)
        self.weather_frame.setMinimumSize(QtCore.QSize(0, 36))
        self.weather_frame.setMaximumSize(QtCore.QSize(16777215, 36))
        self.weather_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weather_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weather_frame.setObjectName("weather_frame")
        self.weather_hlayout = QtWidgets.QHBoxLayout(self.weather_frame)
        self.weather_hlayout.setContentsMargins(0, 0, 0, 0)
        self.weather_hlayout.setSpacing(0)
        self.weather_hlayout.setObjectName("weather_hlayout")
        self.weather_btn = QtWidgets.QPushButton(self.weather_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_btn.sizePolicy().hasHeightForWidth())
        self.weather_btn.setSizePolicy(sizePolicy)
        self.weather_btn.setMinimumSize(QtCore.QSize(0, 34))
        self.weather_btn.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weather_btn.setFont(font)
        self.weather_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.weather_btn.setStyleSheet("text-align: right;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/10d@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_btn.setIcon(icon)
        self.weather_btn.setIconSize(QtCore.QSize(36, 36))
        self.weather_btn.setObjectName("weather_btn")
        self.weather_hlayout.addWidget(self.weather_btn)
        self.button_frame_vlayout.addWidget(self.weather_frame)
        self.scroll_area_vlayout.addWidget(self.button_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.scroll_area_vlayout.addItem(spacerItem)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.slider_vlayout.addWidget(self.scroll_area)
        self.main_hlayout.addWidget(self.slider)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy)
        self.main_widget.setObjectName("main_widget")
        self.main_widget_vlayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.main_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.main_widget_vlayout.setSpacing(0)
        self.main_widget_vlayout.setObjectName("main_widget_vlayout")
        self.stacked_widget = QtWidgets.QStackedWidget(self.main_widget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.page_vlayout = QtWidgets.QVBoxLayout(self.page)
        self.page_vlayout.setContentsMargins(0, 0, 0, 0)
        self.page_vlayout.setSpacing(0)
        self.page_vlayout.setObjectName("page_vlayout")
        self.upper_page_widget = QtWidgets.QWidget(self.page)
        self.upper_page_widget.setMinimumSize(QtCore.QSize(0, 54))
        self.upper_page_widget.setMaximumSize(QtCore.QSize(16777215, 54))
        self.upper_page_widget.setObjectName("upper_page_widget")
        self.upper_page_hlayout = QtWidgets.QHBoxLayout(self.upper_page_widget)
        self.upper_page_hlayout.setContentsMargins(10, 0, 15, 0)
        self.upper_page_hlayout.setSpacing(0)
        self.upper_page_hlayout.setObjectName("upper_page_hlayout")
        self.slider_btn = QtWidgets.QPushButton(self.upper_page_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_btn.sizePolicy().hasHeightForWidth())
        self.slider_btn.setSizePolicy(sizePolicy)
        self.slider_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.slider_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.slider_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.slider_btn.setStyleSheet("")
        self.slider_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/slider_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slider_btn.setIcon(icon1)
        self.slider_btn.setIconSize(QtCore.QSize(45, 45))
        self.slider_btn.setObjectName("slider_btn")
        self.upper_page_hlayout.addWidget(self.slider_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.upper_page_hlayout.addItem(spacerItem1)
        self.weather_line_edit = QtWidgets.QLineEdit(self.upper_page_widget)
        self.weather_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.weather_line_edit.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weather_line_edit.setFont(font)
        self.weather_line_edit.setStyleSheet("border: 1px solid white;")
        self.weather_line_edit.setObjectName("weather_line_edit")
        self.upper_page_hlayout.addWidget(self.weather_line_edit)
        self.page_vlayout.addWidget(self.upper_page_widget)
        self.main_page_widget = QtWidgets.QWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_page_widget.sizePolicy().hasHeightForWidth())
        self.main_page_widget.setSizePolicy(sizePolicy)
        self.main_page_widget.setObjectName("main_page_widget")
        self.main_page_vlayout = QtWidgets.QVBoxLayout(self.main_page_widget)
        self.main_page_vlayout.setContentsMargins(45, 0, 45, 0)
        self.main_page_vlayout.setSpacing(0)
        self.main_page_vlayout.setObjectName("main_page_vlayout")
        self.city_label = QtWidgets.QLabel(self.main_page_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_label.sizePolicy().hasHeightForWidth())
        self.city_label.setSizePolicy(sizePolicy)
        self.city_label.setMinimumSize(QtCore.QSize(0, 38))
        self.city_label.setMaximumSize(QtCore.QSize(16777215, 38))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.main_page_vlayout.addWidget(self.city_label)
        self.temp_label = QtWidgets.QLabel(self.main_page_widget)
        self.temp_label.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.temp_label.setFont(font)
        self.temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_label.setObjectName("temp_label")
        self.main_page_vlayout.addWidget(self.temp_label)
        self.weather_label = QtWidgets.QLabel(self.main_page_widget)
        self.weather_label.setMinimumSize(QtCore.QSize(0, 23))
        self.weather_label.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weather_label.setFont(font)
        self.weather_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.weather_label.setObjectName("weather_label")
        self.main_page_vlayout.addWidget(self.weather_label)
        self.max_min_temp_label = QtWidgets.QLabel(self.main_page_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_min_temp_label.sizePolicy().hasHeightForWidth())
        self.max_min_temp_label.setSizePolicy(sizePolicy)
        self.max_min_temp_label.setMinimumSize(QtCore.QSize(0, 18))
        self.max_min_temp_label.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.max_min_temp_label.setFont(font)
        self.max_min_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.max_min_temp_label.setObjectName("max_min_temp_label")
        self.main_page_vlayout.addWidget(self.max_min_temp_label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.main_page_vlayout.addItem(spacerItem2)
        self.hourly_widget = QtWidgets.QWidget(self.main_page_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourly_widget.sizePolicy().hasHeightForWidth())
        self.hourly_widget.setSizePolicy(sizePolicy)
        self.hourly_widget.setMinimumSize(QtCore.QSize(0, 145))
        self.hourly_widget.setMaximumSize(QtCore.QSize(16777215, 145))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.hourly_widget.setFont(font)
        self.hourly_widget.setStyleSheet("#hourly_widget{\n"
"    background: rgba(255, 255, 255, 64);\n"
"    border-radius: 10px;\n"
"}")
        self.hourly_widget.setObjectName("hourly_widget")
        self.hourly_vlayout = QtWidgets.QVBoxLayout(self.hourly_widget)
        self.hourly_vlayout.setContentsMargins(6, 0, 0, 0)
        self.hourly_vlayout.setObjectName("hourly_vlayout")
        self.hourly_frame = QtWidgets.QFrame(self.hourly_widget)
        self.hourly_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.hourly_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.hourly_frame.setStyleSheet("#hourly_frame{\n"
"    border-bottom: 1px solid #d5d6d7;\n"
"}")
        self.hourly_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hourly_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hourly_frame.setObjectName("hourly_frame")
        self.hourly_frame_hlayout = QtWidgets.QHBoxLayout(self.hourly_frame)
        self.hourly_frame_hlayout.setContentsMargins(0, 0, 0, 0)
        self.hourly_frame_hlayout.setSpacing(7)
        self.hourly_frame_hlayout.setObjectName("hourly_frame_hlayout")
        self.hourly_icon_label = QtWidgets.QLabel(self.hourly_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourly_icon_label.sizePolicy().hasHeightForWidth())
        self.hourly_icon_label.setSizePolicy(sizePolicy)
        self.hourly_icon_label.setMinimumSize(QtCore.QSize(15, 15))
        self.hourly_icon_label.setMaximumSize(QtCore.QSize(15, 15))
        self.hourly_icon_label.setText("")
        self.hourly_icon_label.setPixmap(QtGui.QPixmap("icons/hour_icon.svg"))
        self.hourly_icon_label.setScaledContents(True)
        self.hourly_icon_label.setObjectName("hourly_icon_label")
        self.hourly_frame_hlayout.addWidget(self.hourly_icon_label)
        self.hourly_label = QtWidgets.QLabel(self.hourly_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hourly_label.setFont(font)
        self.hourly_label.setStyleSheet("color: #d5d6d7;")
        self.hourly_label.setObjectName("hourly_label")
        self.hourly_frame_hlayout.addWidget(self.hourly_label)
        self.hourly_vlayout.addWidget(self.hourly_frame)

        self.hourly_scroll_area = QtWidgets.QScrollArea(self.hourly_widget)
        self.hourly_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hourly_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hourly_scroll_area.setWidgetResizable(True)
        self.hourly_scroll_area.setObjectName("hourly_scroll_area")
        self.hourly_scroll_area_widget = QtWidgets.QWidget()
        self.hourly_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 480, 109))
        self.hourly_scroll_area_widget.setObjectName("hourly_scroll_area_widget")
        self.hourly_scroll_area_hlayout = QtWidgets.QHBoxLayout(self.hourly_scroll_area_widget)
        self.hourly_scroll_area_hlayout.setContentsMargins(0, 0, 0, -1)
        self.hourly_scroll_area_hlayout.setSpacing(2)
        self.hourly_scroll_area_hlayout.setObjectName("hourly_scroll_area_hlayout")
        self.hourly_elem_frame = QtWidgets.QFrame(self.hourly_scroll_area_widget)
        self.hourly_elem_frame.setMinimumSize(QtCore.QSize(58, 90))
        self.hourly_elem_frame.setMaximumSize(QtCore.QSize(58, 90))
        self.hourly_elem_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hourly_elem_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hourly_elem_frame.setObjectName("hourly_elem_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.hourly_elem_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hourly_time_label = QtWidgets.QLabel(self.hourly_elem_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hourly_time_label.setFont(font)
        self.hourly_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hourly_time_label.setObjectName("hourly_time_label")
        self.verticalLayout.addWidget(self.hourly_time_label)
        self.hourly_weather_label = QtWidgets.QLabel(self.hourly_elem_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourly_weather_label.sizePolicy().hasHeightForWidth())
        self.hourly_weather_label.setSizePolicy(sizePolicy)
        self.hourly_weather_label.setMinimumSize(QtCore.QSize(40, 40))
        self.hourly_weather_label.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hourly_weather_label.setFont(font)
        self.hourly_weather_label.setText("")
        self.hourly_weather_label.setPixmap(QtGui.QPixmap("icons/01n.png"))
        self.hourly_weather_label.setScaledContents(True)
        self.hourly_weather_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hourly_weather_label.setObjectName("hourly_weather_label")
        self.verticalLayout.addWidget(self.hourly_weather_label, 0, QtCore.Qt.AlignHCenter)
        self.hourly_temp_label = QtWidgets.QLabel(self.hourly_elem_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hourly_temp_label.setFont(font)
        self.hourly_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hourly_temp_label.setObjectName("hourly_temp_label")
        self.verticalLayout.addWidget(self.hourly_temp_label)
        self.hourly_scroll_area_hlayout.addWidget(self.hourly_elem_frame)
        self.hourly_scroll_area.setWidget(self.hourly_scroll_area_widget)
        self.hourly_vlayout.addWidget(self.hourly_scroll_area)
        self.main_page_vlayout.addWidget(self.hourly_widget)
        self.widget_2 = QtWidgets.QWidget(self.main_page_widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(100, 40, 87, 106))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 69, 69))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.main_page_vlayout.addWidget(self.widget_2)
        self.page_vlayout.addWidget(self.main_page_widget)
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("background-color: green;\n"
"")
        self.page_2.setObjectName("page_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stacked_widget.addWidget(self.page_2)
        self.main_widget_vlayout.addWidget(self.stacked_widget)
        self.main_hlayout.addWidget(self.main_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.city_btn.setText(_translate("MainWindow", "Текущее место"))
        self.time_btn.setText(_translate("MainWindow", "00:00"))
        self.temp_btn.setText(_translate("MainWindow", "22°"))
        self.weather_btn.setText(_translate("MainWindow", "Макс: 28° | Мин: 22°"))
        self.city_label.setText(_translate("MainWindow", "Кудрово"))
        self.temp_label.setText(_translate("MainWindow", "17°"))
        self.weather_label.setText(_translate("MainWindow", "Солнечно"))
        self.max_min_temp_label.setText(_translate("MainWindow", "Макс: 22°, мин: 12°"))
        self.hourly_label.setText(_translate("MainWindow", "Прогноз на 48 часов:"))
        self.hourly_time_label.setText(_translate("MainWindow", "21"))
        self.hourly_temp_label.setText(_translate("MainWindow", "16°"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
