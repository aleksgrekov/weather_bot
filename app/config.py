import os

from dotenv import find_dotenv, load_dotenv

"""
Модуль для загрузки и обработки переменных окружения.

Описание:
- vars_list: Список необходимых переменных окружения, которые должны быть заданы в системе или файле .env.
- ENVS: Словарь для хранения загруженных переменных окружения.

Функции:
- Если файл .env найден, переменные окружения загружаются и добавляются в ENVS. В противном случае программа завершает работу.
"""

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

vars_list = ['BOT_TOKEN', 'API_KEY', 'BASE_URL']

ENVS = dict()
for element in vars_list:
    value = os.getenv(element)
    if value:
        ENVS[element] = value
    else:
        exit('{} отсутствует в переменных окружения'.format(element))
