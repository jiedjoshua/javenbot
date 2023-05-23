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
schedule.every().day.at('23:28').do(asyncio.run, send_lunch_reminder())

# Infinite loop to continuously check for scheduled tasks
async def run_schedule():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

# Run the schedule in an asyncio event loop
async def main():
    await asyncio.gather(run_schedule())

# Start the asyncio event loop
if __name__ == '__main__':
    asyncio.run(main())
