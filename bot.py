import random
import telebot

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечать все добавленные задачи.
/exit - выход из программы.
/random - добавить случайную задачу на Сегодня.
"""

RANDOM_TASKS = [
    "Записаться куда-нибудь",
    "Написать Гвидо письмо",
    "Покормить кошку",
    "Помыть машину",
]

token = ""
bot = telebot.TeleBot(token)
my_name = "Юля"
tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    text = "Задача " + task + " добавлена на дату " + date
    add_todo(date, task)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    text = "Задача " + task + " добавлена на дату " + date
    add_todo(date, task)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Задач на эту дату нет"
        bot.send_message(message.chat.id, text)

# @bot.message_handler(content_types=["text"])
# def echo(message):
#     if my_name in message.text:
#         text = "Ба! Знакомые все лица"
#     else:
#         text = message.text
#     bot.send_message(message.chat.id, text)


# Постоянно обращается к серверам Telegram
bot.polling(none_stop=True)
