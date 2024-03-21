import os,random
import telebot,array
import pyqrcode
from pyqrcode import QRCode
from jdatetime import date
bot = telebot.TeleBot("6941726543:AAFX0pFk_nqZnNNwgS583ClBPOynd_wNwOk", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "  سلام")
    global stat
    stat = ""

@bot.message_handler(commands=['help'])
def help(message):
    global stat
    stat = ""
    bot.send_message(message.chat.id, "command /start: print welcome with user name (e.g. Hello Sajjad, Welcome to this bot).\
command /game: Run the guessing number game. The user guesses a number and the bot guides (go up, go down, you win) - while playing, a new game button should be seen at the bottom.\
command /age: Get the date of birth in Hijri and calculate the age. (Hint: Checkout @pylearn page in Instagram)\
command /voice: Get a sentence in English from the user and convert it to voice.\
command /max: Receive an array from the user and print the largest value. numbers should seperate with comma, e.g. 14,7,78,15,8,19,20.\
command /argmax: Get an array from the user and print the index of the largest value.\
command /qrcode: Get a string from the user and generate its qrcode. command help/ Display the above description.")
@bot.message_handler(commands=['max'])
def send_welcome(message):
    bot.send_message(message.chat.id, "  مجموعه ای از اعداد را با کاما جدا نموده و وارد نمایید")
    global state
    state = "max"
@bot.message_handler(commands=['argmax'])
def argmax(message):
    bot.send_message(message.chat.id, "  مجموعه ای از اعداد را با کاما جدا نموده و وارد نمایید!")
    global state
    state = "argmax"
@bot.message_handler(commands=['qrcode'])
def qrcode(message):
    bot.send_message(message.chat.id, " یک رشته جهت تولیدQRCODE ارسال کنید")
    global state
    state = "qrcode"


@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, "  عدد بین 0 تا 20 حدس بزن")
    global state,random_num
    state = "game"
    random_num = random.randint(0, 20)
    print(random_num )
@bot.message_handler(commands=['age'])
def age(message):
	global state
	state = "age"
	bot.send_message(message.chat.id, "تاریخ تولد خود را به شمسی وارد نمایید")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global random_number, state

    if state == "game":
            if int(message.text) > random_num:
                bot.send_message(message.chat.id, "low")
            elif int(message.text) < random_num:
                bot.send_message(message.chat.id, "hight")
            elif int(message.text) == random_num:
                bot.send_message(message.chat.id, "you win")
                game(message)

    if state == "age":
            day, month, year = message.text.split("/")
            birthdate = date(int(year), int(month), int(day))
            today = date.today()
            age =  today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            bot.send_message(message.chat.id, f"سن شما {age} سال هست")

    if state == "max":
        grades_str = message.text
        grades_list = grades_str.split(',')
        a = array.array('i', [])
        j = 0
        for i in grades_list:
            a.append(int(i))
            print(a[j])
            j = j + 1
        print(max(a))
        bot.send_message(message.chat.id, max(a))
    if state == "argmax":
        grades_str = message.text
        grades_list = grades_str.split(',')
        a = array.array('i', [])
        j = 0
        for i in grades_list:
            a.append(int(i))
            print(a[j])
            j = j + 1
        print(a.index(max(a)))
        bot.send_message(message.chat.id, a.index(max(a)))
    if state == "qrcode":
        dest =message.text
        if os.path.isdir('photo.png'):
            s.remove('photo.png')
        myQR = QRCode(dest)
        myQR.png('photo.png', scale=8)
        photo = open('photo.png', 'rb')
        bot.send_photo(message.chat.id,photo)
bot.infinity_polling()
# @bot.message_handler(commands=['test'])
# def send_key(message):
#     buttons = telebot.types.InlineKeyboardMarkup(row_width=3)
#     btn_1 = telebot.types.InlineKeyboardButton('1',callback_data='1')
#     btn_2 = telebot.types.InlineKeyboardButton('2',callback_data='2')
#     btn_3 = telebot.types.InlineKeyboardButton('3',callback_data='3')
#     buttons.add(btn_1,btn_2,btn_3)
#     chat_id = message.chat.id
#     bot.send_message(chat_id,"text",reply_markup=buttons)
# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):
#     if call.data == '1':
#         bot.send_message(chat_id=call.message.chat.id,text="1")
#     if call.data == '2':
#         bot.send_message(chat_id=call.message.chat.id,text="2")
#     if call.data == '3':
#         bot.send_message(chat_id=call.message.chat.id,text="3")









#  دلبخواهی سرچ در فایل انجام دادم
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     code=message.text
#     checkcode=code.find('*')
#     print(code)
#     print(checkcode)
#     if checkcode!=-1:
#         file = open(r"F:\python\telbot\ghaflanko_bot\1.txt", "rt", encoding='utf-8')
#         filestr1 = file.read()
#         i = filestr1.find(code)
#         print(i)
#         s1 = ''
#         if i != -1:
#             while True:
#                 s1 = s1 + filestr1[i]
#                 i = i + 1
#                 if filestr1[i] == '#':
#                       break
#         else:
#             bot.send_message(message.chat.id, "!کد ملی اشتباه است")
#         file.close()
#         bot.send_message(message.chat.id, s1)
#     else:
#         bot.send_message(message.chat.id, "کد ملی اشتباه است")






