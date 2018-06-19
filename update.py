import urllib.request
import json

from urls import *  # Инмпортируем все с файла ссылок
from datetime import datetime, timedelta
from bot import bot, r

def check_new_day(check):
    weekday_today = int((datetime.now() + timedelta(hours=3)).weekday())

    r.set('weekday', weekday_today)
    if check == "группы":
        with urllib.request.urlopen(STUDENT_LIST) as url:
            r.set("STUDENT_LIST", url.read().decode())
            print("Группы обновлены")
        with urllib.request.urlopen(TEACHER_LIST) as url:
            r.set("TEACHER_LIST", url.read().decode())
            print("Преподователи обновлены")
        with urllib.request.urlopen(TEACHER_LIST_UKR) as url:
            r.set("TEACHER_LIST_UKR", url.read().decode())
            print("Преподаватели (укр) обновлены")

    # try:
    #     if int(r.get('weekday')) != weekday_today:
    #         print("Дни недели не совпадают")
    #         r.set('weekday', weekday_today)
    #         if check == "расписание":
    #             with urllib.request.urlopen(STUDENT_SHEDULE):
    #                 print("Расписание студентов обновленно")
    #             with urllib.request.urlopen(TEACHER_SCHEDULE):
    #                 print("Расписание преподователей обновленно")
    #         elif check == "группы":
    #             with urllib.request.urlopen(STUDENT_LIST) as url:
    #                 r.set("STUDENT_LIST", json.loads(url.read().decode()))
    #                 print("Группы обновлены")
    #             with urllib.request.urlopen(TEACHER_LIST) as url:
    #                 r.set("TEACHER_LIST", json.loads(url.read().decode()))
    #                 print("Преподователи обновлены")
    #             with urllib.request.urlopen(TEACHER_LIST_UKR) as url:
    #                 r.set("TEACHER_LIST_UKR", json.loads(url.read().decode()))
    #                 print("Преподаватели (укр) обновлены")
    # except Exception:
    #     r.set('weekday', weekday_today)