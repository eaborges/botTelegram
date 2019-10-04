from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, BASE_HTTP_URL
import json
from pprint import pprint

with open('data.json') as archive:
    data =  json.loads(archive)

def start(update, context):
    msg = "Olá, que bom que você irá participar do FEMTEC - BA!\n\n SELECIONE A PROGRAMAÇÃO:\n /1 - Bloco Cubos\n /2 - Bloco Sanar\n /3 - Bloco Solutis"
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)

def one(update, context):
    msg = group
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)
    
def http_cats(update, context, args):
    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=BASE_HTTP_URL + args[0]
    )

def unknown(update, context):
    msg = "Ainda estou aprendendo... sou praticamente uma bebezinha."
    link = "http://mundoanimal.net.br/wp-content/uploads/2016/01/gata-femea.jpg"
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)
    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=link
    )

    

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        CommandHandler('1', one)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()

