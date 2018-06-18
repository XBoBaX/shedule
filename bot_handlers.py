import urllib.request

from bot import bot, r  # Импортируем объект бота
from log import *
from messages import *  # Инмпортируем все с файла сообщений
from urls import *  # Инмпортируем все с файла ссылок


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
    check_new_day()
    bot.send_message(message.chat.id, message.text)


def check_new_day():
    weekday_today = int((datetime.now() + timedelta(hours=3)).weekday())
    print(weekday_today)
    try:
        if int(r.get('weekday')) != weekday_today:
            print("Дни недели не совпадают")
            r.set('weekday', weekday_today)
            with urllib.request.urlopen(STUDENT_SHEDULE) as url:
                print("Расписание студентов обновленно")
            with urllib.request.urlopen(TEACHER_SCHEDULE) as url:
                print("Расписание преподователей обновленно")
    except Exception:
        r.set('weekday', weekday_today)


if __name__ == '__main__':
    bot.polling(none_stop=True)
