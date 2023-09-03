from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"Alert on {data['ticker']}! Current price is {data['close']} at {data['time']}."
    send_telegram_message(message)
    return jsonify(success=True)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run()
