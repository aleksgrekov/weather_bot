import aiohttp
import json

from typing import Dict, Union, Any

from app.config import ENVS
from geopy.geocoders import Nominatim

"""
Модуль для обработки бизнес-логики бота, связанной с получением данных о погоде.

Описание:
- geolocator: Объект для получения координат городов по их названию.
- get_weather: Асинхронная функция для получения данных о погоде через Yandex Weather API.

Функции:
- get_weather: Выполняет запрос на API для получения данных о погоде в заданном городе, возвращает словарь с информацией о погоде.
"""

geolocator = Nominatim(user_agent="my_weather_bot")


async def get_weather(city: str) -> Union[Dict[str, Any], None]:
    location = geolocator.geocode(city)

    if not location:
        return None

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        params = {'lat': location.latitude, 'lon': location.longitude}
        headers = {
            'X-Yandex-Weather-Key': ENVS.get("API_KEY")
        }
        async with client.get(url=ENVS.get('BASE_URL'), params=params, headers=headers) as response:
            if response.status == 200:
                result = await response.read()
                data_dict = json.loads(result).get('fact')

                weather_dict = {
                    'temp': data_dict.get('temp'),
                    'feels_like': data_dict.get('feels_like'),
                    'humidity': data_dict.get('humidity'),
                    'wind_speed': data_dict.get('wind_speed')
                }
                return weather_dict
            else:
                return None
