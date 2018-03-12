import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

updater = Updater(token='459744558:AAEWYIqK8c-VTomDzIm_4Vre0f-bCJL0JXs')
dispatcher = updater.dispatcher


def roll(s):
    Splitter = 'd'
    MiddleCase = s.split(Splitter)
    CubeMass = int(MiddleCase[1])
    CubeNum = int(MiddleCase[0])
    finalCase = []

    for i in range(CubeNum):
        CurrentCube = random.randint(1, CubeMass)
        CurrentCube = str(CurrentCube)
        finalCase.append(CurrentCube)
    print(finalCase)
    return str(finalCase)


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hey")
    bot.send_message(chat_id=update.message.chat_id, text="hey")
    keyboar(bot, update)
    return update.message.text


def keyboar(bot, update):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    bot.send_message(chat_id=update.message.chat_id, reply_markup=keyboard)


def button(bot, update):
    query = update.callback_query

    bot.send_message(text="Choice : {}".format(query.data),
                     chat_id=query.message.chat_id,
                     message_id=query.message.message_id)
def textMessage(bot, update):
    dd=roll(update.message.text)
    response = 'Результат ' + dd
    bot.send_message(chat_id=update.message.chat_id, text=response)

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
callback_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(callback_handler)

updater.start_polling(clean=True)
