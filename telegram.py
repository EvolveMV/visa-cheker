import requests

BOT_TOKEN = "8153736625:AAF8UWF9HW1X1Vbr0bp1l-JHZWNaaqIeV9Q"
USER_CHAT_ID = "394276302"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": USER_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        print("Telegram response:", response.json())
    except Exception as e:
        print("Telegram error:", e)
