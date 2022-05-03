from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

from scraper import Scraper

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='5221627240:AAF7diRoHNCuyVfYGsKJodTv9gIif6Cc-1U')

scraper = Scraper()

dp = updater.dispatcher

def varaukset(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=scraper.scrape())
    
varaukset_handler = CommandHandler('varaukset', varaukset)
dp.add_handler(varaukset_handler)

updater.start_polling()

#api token 5221627240:AAF7diRoHNCuyVfYGsKJodTv9gIif6Cc-1U

