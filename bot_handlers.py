from log import *
from messages import *  # Импортируем все с файла сообщений
from update import *  #
import telebot


def keyboard_start(message):
    check_new_day("группы")
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('1 курс', '2 курс', '3 курс')
    keyboard.row('4 курс', '5 курс', '6 курс')
    keyboard.row('7 курс', 'Преподаватели')
    print(message.from_user.id)
    
    msg = bot.send_message(message.from_user.id, "Выберите нужный курс", reply_markup=keyboard)
    bot.register_next_step_handler(msg, select_group)


def select_group(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    print("111111111")
    print(message.text)
    group_list = json.loads(r.get("STUDENT_LIST"))
    print(group_list)
    if message.text == "1 курс":
        for ch in group_list:
            print(ch)


@bot.message_handler(commands=['start'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    # bot.send_message(message.chat.id, HELLO_MESSAGE)
    keyboard_start(message)
    # log(message, HELLO_MESSAGE)


@bot.message_handler(commands=['updates'])
# Выполняется, когда пользователь нажимает на updates
def send_updates(message):
    bot.send_message(message.chat.id, UPDATES_MESSAGE)


@bot.message_handler(content_types=["text"])  # Любой текст
def repeat_all_messages(message):
    # check_new_day("расписание")
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
