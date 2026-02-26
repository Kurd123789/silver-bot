import requests
import os

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = "@xkalola"

def get_silver():
    url = "https://api.goldapi.io/api/XAG/USD"
    headers = {"x-access-token": os.environ['GOLD_API']}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data["price"], data["price_change"]

price, change = get_silver()

# هێمای زیادبوون یان کەمبوون
if change > 0:
    arrow = "🔺"
elif change < 0:
    arrow = "🔻"
else:
    arrow = "➖"

# حسابی کیلۆ
ounce_to_kg = 32.1507
price_per_kg = round(price * ounce_to_kg, 2)

message = f"""
📊 نرخی ئێستای زیو (Silver)

💵 ئۆنسە: {price} USD
{arrow} گۆڕانکاری: {change}

💰 کیلۆ: {price_per_kg} USD
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
