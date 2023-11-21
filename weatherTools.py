import geocoder
import requests
import gettext
from PyQt5.QtWidgets import QMessageBox
from collections import namedtuple


WeatherDataTuple = namedtuple("WeatherData", ["cur_temp", "max_temp", "min_temp",
                                              "current_weather", "hourly", "daily",
                                              "timezone_offset", "icon"])


def createInternetWarningWindow():
    def btnsWork(btn):
        if btn.text() == "Retry":
            pass
        else:
            exit(1)

    error = QMessageBox()
    error.setWindowTitle("Нет подключения к интернету")
    error.setText("Проверьте подключение к интернету и нажмите Retry\nЕсли хотите закрыть приложение, нажмите Ok")
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Retry | QMessageBox.Ok)
    error.setDefaultButton(QMessageBox.Retry)
    error.buttonClicked.connect(btnsWork)
    error.exec()


def getWeatherData(lat: float, lon: float) -> WeatherDataTuple:
    weather_translator = gettext.translation('weather', './locale', languages=['ru'])
    weather_translator.install()
    try:
        full_data = requests.get(f"https://openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid"
                                 f"=439d4b804bc8187953eb36d2a8c26a02").json()
        weather_data = WeatherDataTuple(cur_temp=int(full_data["current"]["temp"]),
                                        max_temp=int(full_data["daily"][0]["temp"]["max"]),
                                        min_temp=int(full_data["daily"][0]["temp"]["min"]),
                                        current_weather=_(full_data["current"]["weather"][0]["description"]),
                                        hourly=full_data["hourly"], daily=full_data["daily"],
                                        icon=full_data["current"]["weather"][0]["icon"],
                                        timezone_offset=full_data["timezone_offset"])

        for i in range(len(weather_data.hourly)):
            weather_data.hourly[i] = {"dt": weather_data.hourly[i]["dt"], "temp": int(weather_data.hourly[i]["temp"]),
                                      "icon": weather_data.hourly[i]["weather"][0]["icon"]}

        for j in range(len(weather_data.daily)):
            weather_data.daily[j] = {"dt": weather_data.daily[j]["dt"],
                                     "icon": weather_data.daily[j]["weather"][0]["icon"],
                                     "average_temp": int(weather_data.daily[j]["temp"]["day"]),
                                     "min_temp": int(weather_data.daily[j]["temp"]["min"]),
                                     "max_temp": int(weather_data.daily[j]["temp"]["max"])}
        return weather_data

    except requests.ConnectionError:
        createInternetWarningWindow()
        return getWeatherData(lat, lon)


def getCurrentLocation():
    location = geocoder.ip('me')

    if location.city is None:
        createInternetWarningWindow()
        return getCurrentLocation()

    return location
