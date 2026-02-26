import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)

bot.send_message(
    chat_id="@xkalola",
    text="🔥 TEST MESSAGE FROM GITHUB ACTIONS 🔥"
)
