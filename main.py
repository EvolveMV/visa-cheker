
import json
import requests
import time
import os
import logging
from datetime import datetime, timedelta
import telegram

# Настройки
CHECK_INTERVAL_MINUTES = 5
DATES_TO_CHECK = 730  # Кол-во дней вперёд (2 года)
LOCATION_ID = 89  # Calgary
SCHEDULE_ID = 69194318
BASE_URL = "https://ais.usvisa-info.com/en-ca/niv/schedule"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

# Загрузка cookies из HAR-файла, экспортированного вручную
def load_cookies():
    with open("cookies.json", "r", encoding="utf-8") as f:
        raw = json.load(f)
    session_cookies = {}
    for entry in raw.get("log", {}).get("entries", []):
        if "cookie" in entry.get("request", {}):
            for cookie in entry["request"]["cookies"]:
                session_cookies[cookie["name"]] = cookie["value"]
    return session_cookies

# Получение доступных слотов на дату
def get_slots(session, date):
    url = f"{BASE_URL}/{SCHEDULE_ID}/appointment/times/{LOCATION_ID}.json?date={date}&appointments[expedite]=false"
    response = session.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Отправка уведомления
def notify(text):
    token = os.environ.get("TG_BOT_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")
    if token and chat_id:
        bot = telegram.Bot(token=token)
        bot.send_message(chat_id=chat_id, text=text)

# Основная логика
def main():
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
                notify(f"🔵 Есть доступные даты на {date_str}: " + ", ".join([s["time"] for s in slots]))
        except Exception as e:
            logging.exception(f"Ошибка на дате {date_str}: {str(e)}")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(CHECK_INTERVAL_MINUTES * 60)
