from setupUi import CustomButton, setupQCompleter
from PyQt5 import QtCore, QtGui, QtWidgets
from WeatherFrame import WeatherFrame
from weatherTools import getWeatherDataAtCurrentPlace, getWeatherData
from filesTools import readCityList
from WeatherPage import WeatherPage
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
                                 "#central_widget{\n"
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
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")

        self.main_hlayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.main_hlayout.setContentsMargins(0, 0, 0, 0)
        self.main_hlayout.setSpacing(0)
        self.main_hlayout.setObjectName("main_hlayout")

        self.is_expanded = True
        self.slider = QtWidgets.QWidget(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy)
        self.slider.setMinimumSize(QtCore.QSize(235, 0))
        self.slider.setMaximumSize(QtCore.QSize(235, 16777215))
        self.slider.setObjectName("slider")

        self.slider_vlayout = QtWidgets.QVBoxLayout(self.slider)
        self.slider_vlayout.setContentsMargins(0, 0, 0, 0)
        self.slider_vlayout.setSpacing(0)

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
        self.current_city_data = getWeatherDataAtCurrentPlace()

        self.current_city_frame = WeatherFrame(self.scroll_area_widget, "Текущее место",
                                               self.current_city_data["cur_temp"],
                                               self.current_city_data["max"],
                                               self.current_city_data["min"],
                                               self.current_city_data["icon"],
                                               self.current_city_data["timezone_offset"],
                                               self.local_timezone_offset)
        self.scroll_area_vlayout.addWidget(self.current_city_frame)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        self.scroll_area_vlayout.addItem(spacerItem)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.slider_vlayout.addWidget(self.scroll_area)
        self.main_hlayout.addWidget(self.slider)
        self.main_widget = QtWidgets.QWidget(self.central_widget)
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

        self.cities_list = readCityList()
        self.completer = setupQCompleter([f"{city['name']}, {city['country']}" for city in self.cities_list])
        self.current_city_page = WeatherPage(self.current_city_data["city"], self.current_city_data["cur_temp"],
                                             self.current_city_data["current_weather"], self.current_city_data["max"],
                                             self.current_city_data["min"],
                                             hourly_list=self.current_city_data["hourly"],
                                             current_city_time_offset=self.current_city_data["timezone_offset"],
                                             local_time_offset=self.local_timezone_offset,
                                             completer=self.completer, is_added=True)
        self.city_pages_list = [self.current_city_page]
        self.added_cities = [self.current_city_frame]
        self.stacked_widget.addWidget(self.current_city_page)

        self.main_widget_vlayout.addWidget(self.stacked_widget)
        self.main_hlayout.addWidget(self.main_widget)
        MainWindow.setCentralWidget(self.central_widget)
        self.current_city_page.slider_btn.released.connect(self.current_city_page.slider_btn.icon_anim.start)
        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)

        #self.current_city_frame.temp_btn.clicked.connect(self.changePage)
        self.current_city_frame.temp_btn.clicked.connect(self.current_city_frame.animButton)
        self.completer.activated.connect(
            lambda: self.createPage(self.city_pages_list[self.stacked_widget.currentIndex()].weather_line_edit.text()))
        self.current_city_page.slider_btn.clicked.connect(self.sliderAnimation)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Прогноз погоды")

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

    def changePage(self, page, index):
        self.stacked_widget.setCurrentIndex(index)
        self.animation_page = QtCore.QPropertyAnimation(page, b"geometry")
        self.animation_page.setDuration(550)

        self.animation_page.setStartValue(
            QtCore.QRect(0, -self.central_widget.height(), self.stacked_widget.width(), self.stacked_widget.height()))

        self.animation_page.setEndValue(
            QtCore.QRect(0, 0, self.stacked_widget.width(), self.stacked_widget.height()))

        self.animation_page.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation_page.start()
        self.city_pages_list[index].slider_btn.clicked.connect(self.sliderAnimation)

        if not self.city_pages_list[-2].getAdd():
            self.stacked_widget.removeWidget(self.city_pages_list[-2])
            del self.city_pages_list[-2]

    def createPage(self, city_country):
        print(city_country)
        city_name, country_name = city_country.split(", ")
        for city in self.cities_list:
            if city["name"] == city_name and city["country"] == country_name:
                weather_data = getWeatherData(city["coord"]["lat"], city["coord"]["lon"])
                self.city_pages_list.append(
                    WeatherPage(city_name, self.current_city_data["cur_temp"],
                                weather_data["current_weather"], weather_data["max"],
                                weather_data["min"],
                                hourly_list=weather_data["hourly"],
                                current_city_time_offset=weather_data["timezone_offset"],
                                local_time_offset=self.local_timezone_offset,
                                completer=self.completer,
                                is_added=False))
                self.stacked_widget.addWidget(self.city_pages_list[-1])
                self.changePage(self.city_pages_list[-1], len(self.city_pages_list) - 1)

                break