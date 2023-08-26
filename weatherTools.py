import geocoder
import requests
import json


def getWeatherData(lat, lon):
    full_data = requests.get(f"https://openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid"
                             f"=439d4b804bc8187953eb36d2a8c26a02").json()
    with open("test.json", "w") as fout:
        json.dump(full_data, fout, ensure_ascii=False, indent="\t")
    data_for_frame = []
    data_for_frame.append(int(full_data["current"]["temp"]))
    data_for_frame.append(int(full_data["daily"][0]["temp"]["max"]))
    data_for_frame.append(int(full_data["daily"][0]["temp"]["min"]))
    data_for_frame.append(full_data["current"]["weather"][0]["icon"])
    data_for_frame.append(full_data["timezone_offset"])
    return data_for_frame


def getWeatherDataAtCurrentPlace():
    g = geocoder.ip('me')
    print(g.city)
    return getWeatherData(*g.latlng)




