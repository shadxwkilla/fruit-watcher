from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def index():
    return "Fruit Watcher is running!"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    text = data.get("text", "🍍 Фрукт заспавнился!")

    response = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )
    
    print("Telegram response:", response.status_code, response.text)  # Для логов Render

    if response.status_code != 200:
        return f"Error sending message: {response.text}", 500

    return "Notification sent!", 200
