import telebot
import psycopg2


bot = telebot.TeleBot('6718371561:AAGrVkk5nOGydblX538jl-hxxoEijYeeJfE')
conn = psycopg2.connect(dbname="postgres", user="postgres", password="root", host="localhost", port="5432")
with conn:
    with conn.cursor() as cursor:
        print("Подключение установлено")
        
@bot.message_handler(commands=['start'])
def main(message):
        bot.send_message(message.chat.id, 'Привет, для начала создай анкету!')

@bot.message_handler(commands=['anketa'])
def main(message):
    bot.send_message(message.chat.id, 'Назови своё имя!')	

def main(message):
    new_cursor = conn.cursor()
    with conn.cursor():
        cursor.execute("INSERT INTO anketa(user_name) VALUES(?)", [message.from_user.id])
        new_cursor.close()    

with conn.cursor() as cur:
    cur.execute("SELECT * FROM anketa")
    rows = cur.fetchall()

print(rows)        
bot.polling(none_stop=True)
