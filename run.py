import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.config import ENVS

"""
Основной файл для запуска бота.

Описание:
- bot: Экземпляр бота, созданный с использованием токена из переменных окружения.
- dp: Диспетчер, который используется для маршрутизации команд и сообщений.

Функции:
- main: Основная асинхронная функция для старта long-polling и подключения маршрутизатора.
"""

bot = Bot(token=ENVS.get('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
