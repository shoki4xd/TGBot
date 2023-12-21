import telebot
bot = telebot.TeleBot('6718371561:AAGrVkk5nOGydblX538jl-hxxoEijYeeJfE')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, для начала создай анкету!')
    

@bot.message_handler(commands=['anketa'])
def main(message):
    bot.send_message(message.chat.id, 'Назови своё имя!')	
    
bot.polling(none_stop=True)