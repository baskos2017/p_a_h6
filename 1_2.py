import aiohttp
import sqlite3
import asyncio
from datetime import datetime
from constant import *

conn = sqlite3.connect('aiohttp_requests_logs.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS aiohttp_requests_logs (
                    id INTEGER PRIMARY KEY,
                    url TEXT,
                    timestamp TEXT,
                    status_code INTEGER
                )''')
conn.commit()

def log_request(url, status_code):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''INSERT INTO aiohttp_requests_logs (url, timestamp, status_code)
                      VALUES (?, ?, ?)''', (url, timestamp, status_code))
    conn.commit()

async def get_content_with_aiohttp(urls):
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(f"Запит до адреси {url}...")
            async with session.get(url) as response:
                if response.status == 200:
                    print(f"Відповідь для адреси {url} отримано зі статусом 200.")
                else:
                    print(f"Отримано відповідь для адреси {url} зі статусом {response.status}.")
                log_request(url, response.status)

if __name__ == "__main__":
    asyncio.run(get_content_with_aiohttp(urls))

conn.close()
