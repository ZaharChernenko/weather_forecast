import json
import os


def checkDirectory(path):
    try:
        os.makedirs(path)

    except FileExistsError:
        print("Directory already exists")


def loadUserData():
    """Returns string"""
    with open("./data/user_data.json", "r", encoding="utf-8") as fin:
        file_check = fin.read().strip()
        return file_check


def readCityList():
    with open("./data/city_list.json", "r", encoding="UTF-8") as fin:
        return json.load(fin)
