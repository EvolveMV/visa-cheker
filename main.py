
import os
import time
import json
import logging
import requests
from datetime import datetime, timedelta
import telegram

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Константы
DATES_TO_CHECK = 10
CHECK_INTERVAL_MINUTES = 5

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def load_cookies():
    with open("cookies.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_slots(session, date):
    url = f"https://ais.usvisa-info.com/en-ca/niv/schedule/{date}"
    response = session.get(url)
    response.raise_for_status()
    return response.json().get("available_slots", [])

def notify(text):
    token = os.environ.get("TG_BOT_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")
    if token and chat_id:
        bot = telegram.Bot(token=token)
        bot.send_message(chat_id=chat_id, text=text)

def main():
    print(f"[{datetime.now()}] Проверка доступных дат...")  # Вывод в логи Railway
    session = requests.Session()
    cookies = load_cookies()
    session.cookies.update(cookies)
    session.headers.update(HEADERS)

    today = datetime.today()
    for i in range(DATES_TO_CHECK):
        date_str = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        try:
            slots = get_slots(session, date_str)
            if slots:
                message = f"🟢 Есть доступные даты: {date_str} - " + ", ".join([s["time"] for s in slots])
                notify(message)
        except Exception as e:
            logging.exception(f"Ошибка на дате {date_str}: {str(e)}")
            time.sleep(1)

if name == "__main__":
    while True:
        main()
        time.sleep(CHECK_INTERVAL_MINUTES * 60)
