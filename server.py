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

        resp = requests.post(
            'https://discordapp.com/api/channels/%s/invites' % os.getenv('CHANNEL_ID'), 
            headers={'Authorization': 'Bot %s' % discordtoken},
            json={'max_uses': 1, 'unique': True, 'expires': 3600})

        inv = resp.json()
        
        if 'code' in inv:
            return json.dumps({'success': True, 'url': inv['code']})
        else:
            print('Error!')
            return json.dumps({'success': False})
    else:
        print('Not granting invite!', respdata)
        return json.dumps({'success': False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
