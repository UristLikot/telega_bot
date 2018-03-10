import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
    bot.send_message(chat_id=update.message.chat_id, text='Задайте значение')
    return update.message.text


def textMessage(bot, update):
    dd=roll(update.message.text)
    response = 'Результат ' + dd
    bot.send_message(chat_id=update.message.chat_id, text=response)


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
