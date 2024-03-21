import telebot
bot = telebot.TeleBot("6941726543:AAFX0pFk_nqZnNNwgS583ClBPOynd_wNwOk", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "  سلام")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "خوبی یا بهتری چاقالللللچه")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    code=message.text
    checkcode=code.find('*')
    print(checkcode)
    if checkcode!=-1:
        file = open(r"F:\python\telbot\ghaflanko_bot\1.txt", "rt", encoding='utf-8')
        filestr1 = file.read()
        i = filestr1.find(code)
        s1 = ''
        if i != -1:
            while True:
                s1 = s1 + filestr1[i]
                i = i + 1
                if filestr1[i] == '#':
                      break
        file.close()
        bot.send_message(message.chat.id, s1)
    else:
        bot.send_message(message.chat.id, "!کد ملی اشتباه است")
bot.infinity_polling()