import telebot
import os

# Fetch API key
API_KEY = os.getenv('TELEBOT_API')

# Initialize bot
bot = telebot.TeleBot(token=API_KEY)


# --- Commands ---
# Start
@bot.message_handler(commands=['start'])
def test(message):
    bot.reply_to(message, 'Hello there!')

# Test
@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, 'OK')


# --- Main---
if __name__ == '__main__':
    print('--- BOT RUNNING ---')
    bot.polling()