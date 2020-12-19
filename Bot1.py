import telebot
from telebot import types
#1277027637:AAEEA0U3hBGXLhHsC-71xjS5_QAmVMglmq0
name = ""
surname =""
age = " "


bot = telebot.TeleBot("1277027637:AAEEA0U3hBGXLhHsC-71xjS5_QAmVMglmq0")
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello krasav4ik")
@bot.message_handler(func=lambda m: True)

def echo_all(message):
    if message.text == "Hello":
        bot.reply_to(message, "What's up bro?")
    elif message.text == "/go":
        bot.send_message(message.from_user.id, "What songs do you like?" )
        bot.register_next_step_handler(message, go_name)
        # bot.reply_to(message, message.text)
def go_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "how about listening to a couple of songs?")
    bot.register_next_step_handler(message, go_surname)
def go_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Are you ready?")
    bot.register_next_step_handler(message, go_age)
def go_age (message):
    global age
    #age = message.texte
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, " ")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Playlist#1", callback_data="yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Playlist#2", callback_data="no")
    keyboard.add(key_no)
    question = "Which" + str(age) + "one will you choose?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard )



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.from_user.id, "A$AP ROCKY - BAMBA/ EMINEM - FAREWELL/ BUGUS - FREE/ BIRD GAMBI - PUFF/ BIG SEAN FEAT. POST MALONE - WOLVES/RAURY - CRYSTAL EXPRESS/REMA - FAME/BOW WOW - I'M A FLIRT/MASEGO - BLACK LOVE/MASEGO - TADOW/GUNNA - DOLLAZ ON MY HEAD/METRO BOOMIN - OVERDUE/21 SAVAGE FEAT. METRO BOOMIN - MR.RIGHT NOW/RUSS - I THOUGT YOU GOT ME /AMINE - CAN'T DECIDE/BLXST - NO LOVE LOST /YSN FLOW - PLAYIN IT COOL/ ROB $TONE-ROLLING $TONE/ KIZARU - BLOCK BABY/SHH - BIIG PIIG")
    elif call.data == "no":
        bot.send_message(call.from_user.id, "DUDEONTHEGUITAR & MONRO - TUGAN JER TOLGAUY/ БАСТА - +100500/JELTOKSAN-CHILL CHILL/HASKI-LUCIFER/BASTA-STARWNO TAK ZHIT/MOFASHI-PROGRAMMNIY SBOY/DARKHAN JUZZ-MEN SALEM JAZAMYN/BOULEVARD DEPO-FRIENDLY FIRE/")

bot.polling()