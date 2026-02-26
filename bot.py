import os
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
GOLD_API = os.getenv("GOLD_API")

bot = Bot(token=BOT_TOKEN)

def get_gold_price():
    url = f"https://www.goldapi.io/api/XAG/USD"
    headers = {
        "x-access-token": GOLD_API,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["price"]

def send_price():
    price = get_gold_price()
    message = f"📊 Silver Price Update\n\n💰 Price: ${price} per ounce"
    
    # 👇 ئێرە CHAT_ID دابنێ
    bot.send_message(chat_id="@xkalola", text=message)

if __name__ == "__main__":
    send_price()
