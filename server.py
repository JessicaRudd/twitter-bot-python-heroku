from os import environ
from flask import Flask
import src.twitter_bot

app = Flask(__name__)

@app.route("/")
def home():
    twitter_bot.tweet_quote()
    return "Tweeting weather and a quote..."

app.run(host='0.0.0.0', port=environ.get('PORT'))
