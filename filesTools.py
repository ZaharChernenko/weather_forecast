import json

def readCityList():
    with open("data/city_list.json", "r", encoding="UTF-8") as fin:
        return json.load(fin)