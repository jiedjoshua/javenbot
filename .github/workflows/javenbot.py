import schedule
import time
from telegram import Bot
import asyncio

# Telegram Bot API token
bot_token = '6196088902:AAHxIuetBvYCnweKh5ZfR41WrmQxxiU3NyI'

# User ID to send the reminder
user_id = '1635615023'

# Function to send the reminder message
async def send_lunch_reminder():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=user_id, text='It\'s lunchtime! Don\'t forget to eat pretty! 🍽️') # type: ignore

# Schedule the reminder to run at 12 PM every day
schedule.every().day.at('22:31').do(asyncio.run, send_lunch_reminder())

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
