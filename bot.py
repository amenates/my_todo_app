import telebot

token = "820556957:AAE8XZ3u7iDrdkPnlPm8t6nAND9BJ_CtC-c"
bot = telebot.TeleBot(token)

my_name = "Юля"


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = "Ба! Знакомые все лица"
    else:
        text = message.text
    bot.send_message(message.chat.id, text)


# Постоянно обращается к серверам Telegram
bot.polling(none_stop=True)
