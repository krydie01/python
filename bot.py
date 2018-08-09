import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
    mytext = "Привет {}! Я бот городской библиотечной системы, я помогу вам найти книги, посмотреть афишу мероприятий итд".format(update.message.chat.first_name)
    update.message.reply_text(mytext)

def main():
    updtr = Updater('648569211:AAGa4KFOd10w5bao34KCQ5r-SkFiFiNjvHs')
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logging.info('bot started')
    main()