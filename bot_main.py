import telebot
import os
import json
import time
from datetime import datetime
from getFile import getFileText

# Fetch API key
API_KEY = os.getenv('TELEBOT_API')

# Initialize bot
bot = telebot.TeleBot(token=API_KEY)

# Read paths
with open('paths.json') as f:
    paths = json.load(f)

# --- Commands ---
# Start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello there!')

# Test
@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, 'OK')
    print('[{0}] Test request'.format(datetime.now()))

# Cronlog
@bot.message_handler(commands=['cronlog'])
def cronlog(message):
    text = getFileText(paths['cron_log_path'], 'tail')
    bot.reply_to(message, text)
    print('[{0}] Cron log requested'.format(datetime.now()))

# --- Main---
if __name__ == '__main__':
    print('--- BOT STARTED [{0}] ---'.format(datetime.now()))
    while True:
        try:
            print('[{0}] Polling started'.format(datetime.now()))
            bot.polling()
            break
        except Exception as e:
            print('[{0}] Error occured, standing by'.format(datetime.now()))
            time.sleep(30)