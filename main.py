import requests
import time
import logging
from variables import headers
from telegram import send_message

URL = "https://ais.usvisa-info.com/en-ca/niv/schedule/{YOUR_SCHEDULE_ID}/appointment"

def check_appointments():
    try:
        response = requests.get(URL, headers=headers)
        if "Available" in response.text or "Date" in response.text:
            send_message("🔔 Найдена доступная дата на сайте записи на визу!")
        else:
            logging.info("Нет доступных дат.")
    except Exception as e:
        logging.error(f"Ошибка при запросе: {e}")

if __name__ == "__main__":
    while True:
        check_appointments()
        time.sleep(300)  # каждые 5 минут
