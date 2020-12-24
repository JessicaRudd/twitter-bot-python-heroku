# Twitter Bot Using Python and Heroku

![Python](https://img.shields.io/badge/Python-v3.8.3-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat) [![Twitter](https://img.shields.io/twitter/follow/funsizeathlete.svg?style=social&label=@funsizeathlete)](https://twitter.com/funsizeathlete)

This is a simple template you can use to build a twitter bot using Python and Heroku. I used it to create [@RResurgens](https://twitter.com/RResurgens). Learn how to make your own [here.](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/) - update this link with my own blog post once complete. 
 
Why build a bot this way?
 
 1. It's quick and easy 
 2. Heroku provides a ready-to-use environment based on containers that makes it easy to deploy code - smaller learning curve than AWS.
 3. I wanted to learn how to pull data using an API, refactor code, and push code to a server (as opposed to just running code locally)
 
## Pre-requisites

To build and use the bot, you'll need to:
 
 1. Create a new Twitter accoun to act as the bot
 2. Register for a [twitter developer account](https://developer.twitter.com/en)  
 3. Create a [twitter app](https://developer.twitter.com/en/portal/projects-and-apps). Make sure to give it **Read and Write** permissions.
 4. Set up a [Heroku account](https://www.heroku.com/)
 5. Intialize git repository in project folder, since Heroku pulls entire projects directly from the working directory of your repository. 
 
## How to use

To make your own bot follow these steps:

1. Clone this repository on your local machine
2. Create a virtual environment in your project's root directory: `python3 -m venv environment && source environment/bin/activate`
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `credentials.py` in the root directory of your project. Put your twitter App keys there (and any other keys required for scraping data if needed). 
    * MAKE SURE TO INCLUDE 'import credentials' import statement in twitter_bot.py
    * THIS IS JUST FOR TESTING. Once everything is tested and ready to deploy, you'll move these to environment variables.
    * ADD THIS FILE TO THE .gitignore so you're not putting your api keys publicly on github!
```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<YOUR_ACCESS_TOKEN_SECRET_HERE>
CONSUMER_KEY=<YOUR_CONSUMER_KEY_HERE>
CONSUMER_SECRET=<YOUR_CONSUMER_SECRET_HERE>
```
5. Make changes in the logic of the bot by modyifing `twitter_bot.py`
6. Test your changes locally by running `python twitter_bot.py` from the root directory of your project

## How to deploy

Once you are happy with your bot:

1. Add any additional packages you used to `requirements.txt`
2. Set up [Heroku account](https://signup.heroku.com/) and install Heroku [command line interface](https://devcenter.heroku.com/articles/heroku-cli)
3. Create a basic web server script
```
from os import environ
from flask import Flask
app = Flask(__name__)
app.run(host= '0.0.0.0', port=environ.get('PORT'))
```
4. Set up a Procfile to tell Heroku what to do with the script and server
```
web: python server.py
worker: python twitter_bot.py
```
5. Update twitter_bot.py so that Heroku can find your API credentials. Make sure to include these imports:
```
import sys
from os import environ
```
... and update where app retrieves credentials (instead of retrieving from credentials.py file they'll now be served as environment variables from within Heroku dashboard...
```
consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']
```
6. Commit and push updated files to local main branch of git repository
7. In command line, in project folder, login to Heroku
```
Heroku login
```
8. Create app in Heroku from within CLI
```
heroku create [app-name]
```
9. Set [environmental variables in Heroku dashboard](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard)
10. Push local git repository to deploy app
```
git push heroku main
```
11. Check Twitter to see if a tweet was sent! You can use Heroku dashboard to check logs, troubleshoot, and add additional functionality like scheduling. HAVE FUN!

## Limitations

Read this before using the bot:

## Future Work

1. Refactoring into python package
2. Deploy using Docker and AWS

## References

*This repository was started as a template from Dylan Castillo: https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda to start my own Twitter bot project

*Weather data is pulled from [OpenWeather](https://home.openweathermap.org/)

*[How to Set up a Twitter Bot with Python and Heroku](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39)

*[How to Make a Twitter Bot in Python With Tweepy](https://realpython.com/twitter-bot-python-tweepy/#deploying-bots-to-a-server-using-docker)

*[Build and Deploy Twitter Bots with Python, Tweepy and PythonAnywhere](https://www.twilio.com/blog/build-deploy-twitter-bots-python-tweepy-pythonanywhere)

*[Making a Quote Tweeting Twitter Bot with Python, Tweepy, and Heroku.](https://medium.com/datadriveninvestor/making-a-quote-tweeting-twitter-bot-with-python-tweepy-and-heroku-69a11cd3f47e)



