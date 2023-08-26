from setupUi import CustomButton, setupQCompleter
from PyQt5 import QtCore, QtGui, QtWidgets
from WeatherFrame import WeatherFrame
from weatherTools import getWeatherDataAtCurrentPlace
from filesTools import readCityList
import time



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
        self.is_expanded = True

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
        self.scroll_area_vlayout.setContentsMargins(15, 20, 0, 0)
        self.scroll_area_vlayout.setSpacing(0)
        self.scroll_area_vlayout.setObjectName("scroll_area_vlayout")

        self.local_timezone_offset = -time.timezone
        self.weather_btn1 = WeatherFrame(self.scroll_area_widget, "Текущее место",
                                         *getWeatherDataAtCurrentPlace(), self.local_timezone_offset)
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

        self.slider_btn.clicked.connect(self.sliderAnimation)
        self.weather_btn1.temp_btn.clicked.connect(self.changePage)
        self.weather_btn1.temp_btn.clicked.connect(self.weather_btn1.animButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))

    def sliderAnimation(self):
        if self.is_expanded:
            self.animation_compression_max = QtCore.QPropertyAnimation(self.slider, b"maximumWidth")
            self.animation_compression_max.setDuration(800)
            self.animation_compression_max.setStartValue(235)
            self.animation_compression_max.setEndValue(0)
            self.animation_compression_max.setEasingCurve(QtCore.QEasingCurve.OutQuart)
            self.animation_compression_max.start()

            self.animation_compression_min = QtCore.QPropertyAnimation(self.slider, b"minimumWidth")
            self.animation_compression_min.setDuration(800)
            self.animation_compression_min.setStartValue(235)
            self.animation_compression_min.setEndValue(0)
            self.animation_compression_min.setEasingCurve(QtCore.QEasingCurve.OutQuart)
            self.animation_compression_min.start()
            self.is_expanded = False

        else:
            self.animation_expansion_max = QtCore.QPropertyAnimation(self.slider, b"maximumWidth")
            self.animation_expansion_max.setDuration(800)
            self.animation_expansion_max.setStartValue(0)
            self.animation_expansion_max.setEndValue(235)
            self.animation_expansion_max.setEasingCurve(QtCore.QEasingCurve.OutBack)
            self.animation_expansion_max.start()

            self.animation_compression_min = QtCore.QPropertyAnimation(self.slider, b"minimumWidth")
            self.animation_compression_min.setDuration(800)
            self.animation_compression_min.setStartValue(0)
            self.animation_compression_min.setEndValue(235)
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
