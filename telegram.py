import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("USER_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, data=payload)
        print("Response:", response.text)
    except Exception as e:
        print("Error sending message:", e)
