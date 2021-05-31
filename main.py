from flask import Flask, request
import os
from bot import racer
import threading
import json
import random
from cryptography.fernet import Fernet
import string
chars = list(string.ascii_letters+string.punctuation+string.digits)
index = chars.index('\'')
del chars[index]
index = chars.index('\"')
del chars[index]
def write_json(data, file='info.json'):
    with open('info.json', 'w') as f:
        json.dump(data, f, indent=4)
key = os.getenv('key')
def encrypt(message):
    """
    Encrypts a message
    """
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    return (encrypted_message.decode())
app = Flask(__name__)
@app.route('/', methods=['POST', 'HEAD'])
def main():
    if request.method == 'POST':
        form = request.form
        try:
            form['key']
        except:
            return 'Wrong password'
        if form['key'] == os.getenv('password'):
            def thebot(server_num=1):
                bot = racer(form['username'], form['password'], int(form['speed']), int(form['accuracy']), int(form['races']), 'true')
                bot.server = server_num
                return bot
            try:
                form['threads']
                for x in range(1, int(form['threads'])+1):
                    thread = threading.Thread(target=thebot(x).startBot)
                    thread.start()
                    thread.join(0.5)
            except:
                thread = threading.Thread(target=thebot().startBot)
                thread.start()
                thread.join(1)
            return "Added bot to queue"
        else:
            return 'Wrong password'
    if request.method == 'HEAD':
        return 'Online!'
'''
@app.route('/accs', methods=['POST'])
def accs():
    form = request.form
    if form['key'] == os.getenv('password'):
        with open('info.json') as f:
            data = json.load(f)
            return data
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)