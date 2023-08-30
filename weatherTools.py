import geocoder
import requests
import gettext
import json
from PyQt5.QtWidgets import QMessageBox

weather_translator = gettext.translation('weather', './locale', languages=['ru'])
weather_translator.install()


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
    error.setStandardButtons(QMessageBox.Retry|QMessageBox.Ok)
    error.setDefaultButton(QMessageBox.Retry)
    error.buttonClicked.connect(btnsWork)
    error.exec()

def getWeatherData(lat, lon):
    try:
        full_data = requests.get(f"https://openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid"
                                 f"=439d4b804bc8187953eb36d2a8c26a02").json()

        with open("test.json", "w", encoding="UTF-8") as fout:
            json.dump(full_data, fout, ensure_ascii=False, indent="\t")
        data_dict = {}
        data_dict["cur_temp"] = int(full_data["current"]["temp"])
        data_dict["max"] = int(full_data["daily"][0]["temp"]["max"])
        data_dict["min"] = int(full_data["daily"][0]["temp"]["min"])
        data_dict["icon"] = full_data["current"]["weather"][0]["icon"]
        data_dict["current_weather"] = _(full_data["current"]["weather"][0]["description"])
        data_dict["timezone_offset"] = full_data["timezone_offset"]
        data_dict["hourly"] = full_data["hourly"]
        for i in range(len(data_dict["hourly"])):
            data_dict["hourly"][i] = {"dt": data_dict["hourly"][i]["dt"], "temp": int(data_dict["hourly"][i]["temp"]),
                                      "icon": data_dict["hourly"][i]["weather"][0]["icon"]}
        return data_dict

    except requests.ConnectionError:
        createInternetWarningWindow()
        return getWeatherData(lat, lon)


def getWeatherDataAtCurrentPlace():
    g = geocoder.ip('me')
    print(g.city)

    if g.city is None:
        createInternetWarningWindow()
        return getWeatherDataAtCurrentPlace()

    else:
        data_dict = getWeatherData(*g.latlng)
        data_dict.update({"city": g.city})
        data_dict.update({"coord": {
            "lat": g.latlng[0],
            "lon": g.latlng[1]
        }})
        return data_dict
