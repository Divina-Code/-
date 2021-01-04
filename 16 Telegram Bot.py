import telebot

bot = telebot.TeleBot("1557028526:AAHbaVZxgZjvEZ2SZ4YnWinwQJYMojBYbkM")




@bot.message_handler(content_types=["text"])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])




bot.polling()
