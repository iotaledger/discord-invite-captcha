from flask import Flask, render_template, request
from dotenv import load_dotenv
import json
import requests
import os

app = Flask(__name__)
#load_dotenv(verbose=True)

@app.route("/")
def index():
    return render_template('index.html', key=os.getenv('SITE_KEY'))
@app.route("/invite", methods=['POST'])
def invite():
    token = request.form['token']
    data = {'secret': os.getenv('SECRET_KEY'), 'response': token}
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    respdata = resp.json()

    if respdata['success']:
        print('Granting invite', respdata)
        
        discordtoken = os.getenv('DISCORD_TOKEN')
        channel_id = os.getenv('CHANNEL_ID')

        headers = {'Authorization': f'Bot {discordtoken}'}
        payload = {'max_uses': 1, 'unique': True, 'max_age': 3600}

        resp = requests.post(
            f'https://discord.com/api/v10/channels/{channel_id}/invites',
            headers=headers,
            json=payload)

        inv = resp.json()
        print("Invite creation response:", inv)

        if 'code' in inv:
            return json.dumps({'success': True, 'url': f"https://discord.gg/{inv['code']}"})
        else:
            return json.dumps({'success': False, 'error': inv})
    else:
        print('Not granting invite!', respdata)
        return json.dumps({'success': False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
