import json
from datetime import datetime

def check_visa_dates():
    print("Загружаем har_dump.json...")

    try:
        with open("har_dump.json", "r", encoding="utf-8") as file:
            har_data = json.load(file)

        print("Файл загружен, начинаем проверку...")

        found_dates = []

        for entry in har_data.get("log", {}).get("entries", []):
            content = entry.get("response", {}).get("content", {}).get("text", "")
            if "2027" in content:
                if (
                    "August" in content or "Jul" in content or "Jun" in content or
                    "May" in content or "Apr" in content
                ):
                    found_dates.append(entry.get("request", {}).get("url", ""))

        if found_dates:
            print("Найдены даты:", found_dates)
            message = "<b>Найдены даты до августа 2027!</b>\n"
            message += "\n".join(found_dates[:5])
            return message

        print("Даты не найдены.")
        return None

    except Exception as e:
        print(f"Ошибка при проверке HAR: {str(e)}")
        return None
