from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
from app.funcs import get_weather

"""
Модуль с обработчиками команд и сообщений для бота.

Описание:
- City: Класс состояний для работы с состояниями FSM (в данном случае ввод города).
- cmd_start: Обработчик команды /start, отправляет приветственное сообщение.
- get_city: Обработчик для запроса города у пользователя.
- get_forecast: Обработчик для получения данных о погоде по введенному пользователем городу.
"""

router = Router()


class City(StatesGroup):
    city = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, {name}👋'
                         '\nЯ бот, который поможет тебе узнать актуальную погоду в любом городе. 🌤'
                         '\nПросто отправь мне название города, и я предоставлю информацию о температуре, влажности и других погодных условиях. ☔️🌞!'.format(
        name=message.from_user.first_name
    ),
        reply_markup=kb.markup
    )


@router.callback_query(F.data == 'weather')
async def get_city(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Выполняю запрос..')
    await state.set_state(City.city)
    await callback.message.answer('Введите название города:')


@router.message(City.city)
async def get_forecast(message: Message, state: FSMContext):
    weather_data = await get_weather(message.text)
    if weather_data:
        await message.reply(f'Погода в городе {message.text.title()}'
                            f'\nТемпература: {weather_data.get('temp')}'
                            f'\nОщущается как: {weather_data.get('feels_like')}'
                            f'\nСкорость ветра: {weather_data.get('wind_speed')}'
                            f'\nВлажность: {weather_data.get('humidity')}',
                            reply_markup=kb.markup)
    else:
        await message.reply('Извините! Ваш город не найден!', reply_markup=kb.markup)
    await state.clear()
