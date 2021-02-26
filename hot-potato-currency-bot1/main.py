from settings.SETTINGS import*

import telebot
from parse.Parse import Parse
from parse.dataPy import Data


@BOT.message_handler(commands=['start'])
def strat_message(message):
    BOT.send_message(message.chat.id, 'Выберите интересующую вас валюту', reply_markup=KEYBOARD_START)


@BOT.message_handler(content_types=['text'])
def get_text_message(message):

    global site,values
    
    if message.text == BUTTON_USD:
        site = Parse(URL_USD).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?',reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_EUR:
        site = Parse(URL_EUR).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?',reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_RUB:
        site = Parse(URL_RUB).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что вас интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_ALL_LIST:
        BOT.send_message(message.chat.id, values.get_all_list(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_BUY_VALUE:
        BOT.send_message(message.chat.id, values.get_best_buy_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_SELL_VALUE:
        BOT.send_message(message.chat.id, values.get_best_sell_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        strat_message(message)


    else:
        BOT.send_message(message.chat.id, 'Я тебя не понимаю, напиши пожалуйста, /start')


BOT.polling()


