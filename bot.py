from mrp import WordParsing
import telebot

bot = telebot.TeleBot('761209182:AAGDUOrDKPqfI2y0kgT9o74ZfXKtovMyLuI')
print(WordParsing("Привет").temp)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id,
                           'Напишите /start для начала работы с ботом, после чего введите нужное вам слово')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Напишите слово')


@bot.message_handler(content_types=["text"])
def start(message):
    word = message.text.lower()
    bot.send_message(message.chat.id, WordParsing(word).temp)


bot.polling(none_stop=True)
