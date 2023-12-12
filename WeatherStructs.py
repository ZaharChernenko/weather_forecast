from typing import NamedTuple


Celcius = int
WeatherType = str


class HourlyWeatherDataElem(NamedTuple):
    dt: int
    temp: Celcius
    icon: str


class DailyWeatherDataElem(NamedTuple):
    dt: int
    average_temp: Celcius
    max_temp: Celcius
    min_temp: Celcius
    icon: str


class FullWeatherData(NamedTuple):
    cur_temp: Celcius
    max_temp: Celcius
    min_temp: Celcius
    cur_weather: WeatherType
    hourly: list[HourlyWeatherDataElem]
    daily: list[DailyWeatherDataElem]
    icon: str
    timezone_offset: int
