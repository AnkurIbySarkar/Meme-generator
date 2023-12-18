from flask import Flask, render_template
import requests
import json

import os

app = Flask(__name__)
# meme_folder = os.path.join('static', 'memes')


@app.route('/')
def index():
    meme_data = requests.get("https://meme-api.com/gimme").json()
    meme_url = meme_data['url']
    return render_template('index.html', meme_url=meme_url)


if __name__ == '__main__':
    app.run(debug=True)
