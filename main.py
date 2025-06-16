from flask import Flask, Response
from threading import Thread
import os
import requests

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')

app = Flask(__name__)

@app.route('/')
def home():
    return Response("<h1>✅ SMC Bot on Render is Alive!</h1>", mimetype='text/html')

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def send_telegram_message(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("[ERROR] Missing Telegram credentials")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        print("[INFO] Alert sent:", response.status_code)
    except Exception as e:
        print("[ERROR]", e)

keep_alive()
send_telegram_message("🚀 Bot SMC di Render sudah aktif dan berhasil terkoneksi ke Telegram!")