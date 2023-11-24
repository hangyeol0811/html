from flask import Flask, render_template, request
import requests
import json
from datetime import datetime

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'https://ptb.discord.com/api/webhooks/1177449124170309692/G8BlkdmQBCRHVh0bXiNtxh_TY4a35fPabfEXLNM8r8UnOarrULX9kcf2sFZ3QvbSqIPW'  # 디스코드 웹훅 URL 입력

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_ticket():
    username = request.form.get('username')
    message = request.form.get('message')

    send_discord_webhook(username, message)

    return 'Success'

def send_discord_webhook(username, message):
    embed = {
        'title': '새로운 문의가 등록되었습니다!',
        'description': f'**유저:** {username}\n**내용:** {message}',
        'color': 0x166cea,  # 임베드 색상
        'timestamp': str(datetime.utcnow()),
    }

    payload = {
        'embeds': [embed],
    }

    headers = {'Content-Type': 'application/json'}
    requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
