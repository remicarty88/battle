import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command  # Новый фильтр для команд
import random

# Установите токен вашего бота
API_TOKEN = '7632557398:AAG2Xztyf8TEdVMVao38UPbSqk8vvrwShvI'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Структура для активных игроков
active_players = {}

# Команда для начала боя
@dp.message(Command('start'))  # Используем Command вместо commands=['start']
async def start_battle(message: types.Message):
    user_id = message.from_user.id
    if user_id not in active_players:
        active_players[user_id] = {'health': 100}
        await message.reply("Вы добавлены в очередь для боя!")
    else:
        await message.reply("Вы уже в бою или в очереди.")

# Логика боя
async def battle(player1, player2):
    while active_players[player1]['health'] > 0 and active_players[player2]['health'] > 0:
        attack = random.randint(5, 20)
        active_players[player2]['health'] -= attack
        if active_players[player2]['health'] <= 0:
            await bot.send_message(player1, "Вы победили!")
            await bot.send_message(player2, "Вы проиграли.")
            break
        player1, player2 = player2, player1  # Переход хода

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
