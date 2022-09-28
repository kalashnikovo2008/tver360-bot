from telebot import TeleBot


bot = TeleBot('5634589264:AAGvedWEvfbndJAIVC_SQBDERojGjbyXOWk')  # Токен бота
TO_CHAT_ID = 482371404          # id чата для пересылки

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Сюда можно прислать любую новость:  текст, фото, видео и аудио. Обязательно пишите место и время, когда это произошло. И не забудьте указать анонимно 😎 или нет 🤪')

@bot.message_handler(content_types=['text', 'photo', 'video', 'audio','document'])
def all_messages(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Принято, спасибо!")

if __name__ == '__main__':
    bot.polling(none_stop=True)
