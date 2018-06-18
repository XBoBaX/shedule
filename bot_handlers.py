from bot import bot, r  # Импортируем объект бота
from log import *
from messages import *  # Инмпортируем все с файла сообщений


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
    weekday_today = datetime.now().weekday()
    print(weekday_today)
    print(r)
    print(r.get('weekday'))
    try:
        if r.get('weekday') != weekday_today:
            r.set({'weekday': weekday_today})
            print("Дни недели не совпадают")
        else:
            print("Дни недели совпадают")
    except Exception:
        r.set({'weekday': weekday_today})
        print("Установили день недели")
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
