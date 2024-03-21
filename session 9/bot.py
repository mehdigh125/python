import telebot
#bot=telebot.Telebot("6941726543:AAFX0pFk_nqZnNNwgS583ClBPOynd_wNwOk",parse_mode=None)
bot = telebot.TeleBot("6941726543:AAFX0pFk_nqZnNNwgS583ClBPOynd_wNwOk", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "hi mehdi?")

@bot.message_handler(commands=[ 'help'])
def send_welcome(message):
	bot.reply_to(message, "در خدمتم سرورم")	

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "این یک پیام ساده است")
bot.infinity_polling()	