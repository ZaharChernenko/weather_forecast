from setupUi import CustomButton, setupQCompleter
from PyQt5 import QtCore, QtGui, QtWidgets
from WeatherFrame import WeatherFrame
from filesTools import readCityList


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
                                 "    margin: 20 0 20 0;\n"
                                 "    border-right: 1px solid rgba(255, 255, 255, 0.5);\n"
                                 "}\n"
                                 "\n"
                                 "#weather_line_edit{\n"
                                 "    border-radius: 3px;\n"
                                 "    padding-left: 2px;\n"
                                 "}"
                                 )
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
        self.slider.setMinimumSize(QtCore.QSize(230, 0))
        self.slider.setMaximumSize(QtCore.QSize(230, 16777215))
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
        self.scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 230, 670))
        self.scroll_area_widget.setObjectName("scroll_area_widget")
        self.scroll_area_vlayout = QtWidgets.QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_vlayout.setContentsMargins(15, 20, 0, 0)
        self.scroll_area_vlayout.setSpacing(0)
        self.scroll_area_vlayout.setObjectName("scroll_area_vlayout")
        self.button_frame = QtWidgets.QFrame(self.scroll_area_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setMinimumSize(QtCore.QSize(200, 79))
        self.button_frame.setMaximumSize(QtCore.QSize(200, 79))
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
        self.weather_btn1 = WeatherFrame(self.scroll_area_widget)
        self.scroll_area_vlayout.addWidget(self.weather_btn1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
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
        self.upper_page_widget.setMinimumSize(QtCore.QSize(0, 65))
        self.upper_page_widget.setMaximumSize(QtCore.QSize(16777215, 65))
        self.upper_page_widget.setObjectName("upper_page_widget")
        self.upper_page_hlayout = QtWidgets.QHBoxLayout(self.upper_page_widget)
        self.upper_page_hlayout.setContentsMargins(15, 0, 20, 0)
        self.upper_page_hlayout.setSpacing(0)
        self.upper_page_hlayout.setObjectName("upper_page_hlayout")
        self.slider_btn = CustomButton(self.upper_page_widget)

        self.upper_page_hlayout.addWidget(self.slider_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.upper_page_hlayout.addItem(spacerItem1)
        self.weather_line_edit = QtWidgets.QLineEdit(self.upper_page_widget)
        self.weather_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.weather_line_edit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.weather_line_edit.setStyleSheet("border: 1px solid white;")
        self.weather_line_edit.setObjectName("weather_line_edit")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weather_line_edit.setFont(font)
        self.weather_line_edit.setPlaceholderText("Поиск:")
        self.city_list = readCityList()
        self.weather_line_edit.setCompleter(setupQCompleter([f"{city['name']}, {city['country']}" for city in self.city_list]))
        self.upper_page_hlayout.addWidget(self.weather_line_edit)

        self.page_vlayout.addWidget(self.upper_page_widget)
        self.widget_2 = QtWidgets.QWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.page_vlayout.addWidget(self.widget_2)
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
        self.slider_btn.released.connect(self.slider_btn.icon_anim.start)
        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        self.is_expanded = True
        self.slider_btn.clicked.connect(self.sliderAnimation)
        self.weather_btn1.temp_btn.clicked.connect(self.changePage)
        self.weather_btn1.temp_btn.clicked.connect(self.weather_btn1.animButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.city_btn.setText(_translate("MainWindow", "Владивосток"))
        self.time_btn.setText(_translate("MainWindow", "00:00"))
        self.temp_btn.setText(_translate("MainWindow", "22°"))
        self.weather_btn.setText(_translate("MainWindow", "Макс: 28° | Мин: 22°"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))

    def sliderAnimation(self):
        if self.is_expanded:
            self.animation_compression_max = QtCore.QPropertyAnimation(self.slider, b"maximumWidth")
            self.animation_compression_max.setDuration(800)
            self.animation_compression_max.setStartValue(230)
            self.animation_compression_max.setEndValue(0)
            self.animation_compression_max.setEasingCurve(QtCore.QEasingCurve.OutQuart)
            self.animation_compression_max.start()

            self.animation_compression_min = QtCore.QPropertyAnimation(self.slider, b"minimumWidth")
            self.animation_compression_min.setDuration(800)
            self.animation_compression_min.setStartValue(230)
            self.animation_compression_min.setEndValue(0)
            self.animation_compression_min.setEasingCurve(QtCore.QEasingCurve.OutQuart)
            self.animation_compression_min.start()
            self.is_expanded = False

        else:
            self.animation_expansion_max = QtCore.QPropertyAnimation(self.slider, b"maximumWidth")
            self.animation_expansion_max.setDuration(800)
            self.animation_expansion_max.setStartValue(0)
            self.animation_expansion_max.setEndValue(230)
            self.animation_expansion_max.setEasingCurve(QtCore.QEasingCurve.OutBack)
            self.animation_expansion_max.start()

            self.animation_compression_min = QtCore.QPropertyAnimation(self.slider, b"minimumWidth")
            self.animation_compression_min.setDuration(800)
            self.animation_compression_min.setStartValue(0)
            self.animation_compression_min.setEndValue(230)
            self.animation_compression_min.setEasingCurve(QtCore.QEasingCurve.OutBack)
            self.animation_compression_min.start()
            self.is_expanded = True

    def changePage(self):
        if self.stacked_widget.currentIndex() == 0:
            self.animation_expansion_max = QtCore.QPropertyAnimation(self.page_2, b"geometry")
            self.stacked_widget.setCurrentIndex(1)
            self.animation_expansion_max.setDuration(800)
            self.animation_expansion_max.setStartValue(
                QtCore.QRect(0, -self.centralwidget.height(), self.stacked_widget.width(),
                             self.stacked_widget.height()))
            self.animation_expansion_max.setEndValue(
                QtCore.QRect(0, 0, self.stacked_widget.width(), self.stacked_widget.height()))
            self.animation_expansion_max.setEasingCurve(QtCore.QEasingCurve.OutBack)
            self.animation_expansion_max.start()


        else:
            self.stacked_widget.setCurrentIndex(0)
