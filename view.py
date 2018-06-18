# from model import BotHandler
# import datetime
# import cherrypy

token = "604891132:AAF4m5OiqhZ_gLj-3QizE84dYL2Lgfl-yvk"
import telebot
import os
from flask import Flask, request

bot = telebot.TeleBot(token)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route("/{0}".format(token), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://shedule0server.herokuapp.com/{0}".format(token))
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))