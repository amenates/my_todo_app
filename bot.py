import telebot

token = ""
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
