import json
from datetime import datetime

def check_visa_dates():
    try:
        with open("har_dump.json", "r", encoding="utf-8") as file:
            har_data = json.load(file)

        # Простая проверка: ищем любые даты до августа 2027
        found_dates = []
        for entry in har_data.get("log", {}).get("entries", []):
            content = entry.get("response", {}).get("content", {}).get("text", "")
            if "2027" in content:
                if "August" in content or "Jul" in content or "Jun" in content or "May" in content or "Apr" in content:
                    found_dates.append(entry.get("request", {}).get("url", ""))

        if found_dates:
            message = "<b>🎯 Найдены даты до августа 2027!</b>
"
            message += "\n".join(found_dates[:5])
            return message
        return None
    except Exception as e:
        return f"Ошибка при проверке HAR: {str(e)}"