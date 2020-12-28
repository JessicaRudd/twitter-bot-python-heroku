#!/usr/bin/env python
# coding: utf-8
import json
import random
import time
import sys
import tweepy
import credentials
import urllib.request
from os import environ
import gc

# CONSUMER_KEY = credentials.CONSUMER_KEY
# CONSUMER_SECRET = credentials.CONSUMER_SECRET
# ACCESS_KEY = credentials.ACCESS_KEY
# ACCESS_SECRET = credentials.ACCESS_KEY_SECRET
# FORECAST_APIKEY = credentials.FORECAST_APIKEY

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
FORECAST_APIKEY = environ['FORECAST_APIKEY']


def get_quotes():
    with open('quotes.json') as f:
        quotes_json = json.load(f)
    return quotes_json['quotes']

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def create_quote():
    quote = get_random_quote()
    quote = """
            {}
            ~{}
            """.format(quote['quote'], quote['author'])
    return quote

def get_weather():
    req = urllib.request.Request(url=f'https://api.openweathermap.org/data/2.5/weather?q=Atlanta&units=imperial&appid='+FORECAST_APIKEY)

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        gc.collect()
    return data

def create_tweet():
        
    data=get_weather()
    temperature = str(int(round(data['main']['temp'])))
    degree_sign = u'\N{DEGREE SIGN}'
    description = data['weather'][0]['description']
    #description = data['current']['weather'][0]['description']

    tweet = "Rise Up ATL Runners! It's currently " + temperature + degree_sign + "F and " + str(description) +". Time for a run!" + create_quote()+"\n #morningmotivation #running #atlanta #atlantatrackclub"

    if len(tweet) > 280:
        tweet = "Rise Up ATL Runners! It's currently " + temperature + degree_sign + "F and " + str(description)+". Time for a run! \n #morningmotivation #running #atlanta #atlantatrackclub"
    
    return tweet

def tweet_quote():
    #interval = 60 * 60 * 12 # tweet every 12 hours

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    tweet = create_tweet()
    api.update_status(tweet)

    #while True:
     #   print('getting a random quote...')        
      #  tweet = create_tweet()
       # api.update_status(tweet)
        #time.sleep(interval) 
    
if __name__ == "__main__":
    tweet_quote()





