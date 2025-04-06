from datetime import datetime

import requests
import time


def get_usd_rate():
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        usd_rate = data['Valute']['USD']['Value']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return date, usd_rate
    except Exception as e:
        print(f"Ошибка при получении курса: {e}")
        return None, None


print(get_usd_rate())
