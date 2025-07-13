import time
from telegram import send_telegram_message
from har_parser import check_visa_dates

# Telegram Token и Chat ID встроены прямо в код
TELEGRAM_TOKEN = "8153736625:AAF8UWF9HWlX1Vbr0bpll-JHZWNaaqIeV9Q"
USER_CHAT_ID = "394276302"

def run_checker():
    message = check_visa_dates()
    if message:
        send_telegram_message(TELEGRAM_TOKEN, USER_CHAT_ID, message)

if __name__ == "__main__":
    while True:
        run_checker()
        time.sleep(300)  # каждые 5 минут