import telebot

from telebot import types

botTimeWeb = telebot.TeleBot('6464043417:AAG7LUtNoSbTXDMPbfwMlD0lt8nLZnQui2A')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, Ассалому алейкум!\nКандай жардам керек?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Телефонумду ондоп бер', callback_data='yes')
    markup.add(button_yes)
    button_why = types.InlineKeyboardButton(text='Телеграм бот жасап бер', callback_data='why')
    markup.add(button_why)
    button_no = types.InlineKeyboardButton(text='Башка жардам керек', callback_data='no')
    markup.add(button_no)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "Менин атым: Манас Кайрылганыныз учун кубанычтамын!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Ссылка:", url="https://t.me/manas_boitov"
                                                                ""))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'why':
            second_mess = "Телеграм бот жасаганга муноздомолорду калтырып кетиниз мен сиз менен байланышам!)"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Телеграм ссылка", url="https://t.me/manas_boitov"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'no':
            second_mess = "Мен сизди угуп жатам койгойунузду айта бериниз"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Кайрылуу телеграм аркылуу", url="https://t.me/manas_boitov"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)


botTimeWeb.infinity_polling()

