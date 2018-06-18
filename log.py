from datetime import datetime


def log(message, answer):
    print("Время: {0}. Сообщение от {1} {2} (id = {3}) \n Текст - {4} \n Наш ответ: {5}".
          format(datetime.now(), message.from_user.first_name, message.from_user.last_name,
                 str(message.from_user.id), message.text, answer))

