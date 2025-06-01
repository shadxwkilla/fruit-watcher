from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("6223928694:AAHlHo3LxZYAv4d28iOjXrqph2buW_aiA1o")
CHAT_ID = os.environ.get("6159204744")

@app.route("/")
def index():
    return "Fruit Watcher is running!"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    text = data.get("text", "🍍 Фрукт заспавнился!")

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )
    return "Notification sent!", 200
