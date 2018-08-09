import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig()

def start_bot(bot, update):
    mytext = "Привет {}! Я бот городской библиотечной системы, я помогу вам найти книги, посмотреть афишу мероприятий итд".format(update.message.chat.first_name)
    update.message.reply_text(mytext)

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    updtr = Updater('648569211:AAGa4KFOd10w5bao34KCQ5r-SkFiFiNjvHs', request_kwargs=PROXY)
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    main()