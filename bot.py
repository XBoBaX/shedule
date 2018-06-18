import telebot
import config  # подключаем конфиг, чтобы взять с него токен бота
import redis  # подключаем БД
import os

r = redis.from_url(os.environ.get("REDIS_URL"), decode_responses=True)
bot = telebot.TeleBot(config.TOKEN)
print(r)
