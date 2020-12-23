#!/usr/bin/env python
# coding: utf-8

# In[30]:


import json
import random
import time
import sys
import tweepy
import credentials
import urllib.request
from os import environ
import gc


# In[6]:


consumer_key = environ['CONSUMER_KEY']
consumer_secret_key = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']
FORECAST_APIKEY = environ['FORECAST_APIKEY']


# In[44]:


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

    tweet = "Rise Up ATL Runners! It's currently " + temperature + degree_sign + "F and " + str(description) +". Time for a run!" + create_quote()

    if len(tweet) > 280:
        tweet = "Rise Up ATL Runners! It's currently " + temperature + degree_sign + "F and " + str(description)+". Time for a run!"
    
    return tweet
 
def tweet_quote():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = create_tweet()
    status = api.update_status(tweet)
    print(status.id)
    
if __name__ == "__main__":
    tweet_quote()

#tweet_quote()
# def send_quote():
#      tweet = create_tweet()
#      status = api.update_status(tweet)
#      print(status.id)


# In[ ]:




