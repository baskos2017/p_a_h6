import requests
import sqlite3
from datetime import datetime
from constant import *

conn = sqlite3.connect('requests_logs.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS requests_logs (
                    id INTEGER PRIMARY KEY,
                    url TEXT,
                    timestamp TEXT,
                    status_code INTEGER
                )''')
conn.commit()

def log_request(url, status_code):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''INSERT INTO requests_logs (url, timestamp, status_code)
                      VALUES (?, ?, ?)''', (url, timestamp, status_code))
    conn.commit()

def get_content_with_requests(urls):
    for url in urls:
        print(f"Запит до адреси {url}...")
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Відповідь для адреси {url} отримано зі статусом 200.")
        else:
            print(f"Отримано відповідь для адреси {url} зі статусом {response.status_code}.")
        log_request(url, response.status_code)

if __name__ == "__main__":
    
    get_content_with_requests(urls)

conn.close()
