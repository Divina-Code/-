import telebot

bot = telebot.TeleBot("1487570771:AAFdxEUG2D7eZT64w8TKQdL5KmplG0AG1lc")



@bot.message_handler(content_types=["text"])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])




bot.polling()
