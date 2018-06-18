from bot import bot  # Импортируем объект бота
from log import *
from messages import *  # Инмпортируем все с файла сообщений

print("1")

@bot.message_handler(commands=['start'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)
    log(message, HELLO_MESSAGE)


@bot.message_handler(commands=['updates'])
# Выполняется, когда пользователь нажимает на updates
def send_updates(message):
    bot.send_message(message.chat.id, UPDATES_MESSAGE)


@bot.message_handler(content_types=["text"])  # Любой текст
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
