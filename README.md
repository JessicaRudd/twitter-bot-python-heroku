# Twitter Bot Using Python and Heroku

![Python](https://img.shields.io/badge/Python-v3.8.3-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat) [![Twitter](https://img.shields.io/twitter/follow/:funsizeathlete.svg?style=social&label=@:funsizeathlete)](https://twitter.com/:funsizeathlete)


*This repository was pulled as a template from Dylan Castillo: https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda to start my own Twitter bot project

This is a simple template you can use to build a twitter bot using Python and Heroku. I used it to create [@RResurgens](https://twitter.com/RResurgens). Learn how to make your own [here.](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/)
 
Why build a bot this way?
 
 1. It's quick and easy 
 2. You have full control over the bot's actions
 3. 
 
## Pre-requisites

To build and use the bot, you'll need to:
 
 1. Register for a [twitter developer account](https://developer.twitter.com/en)  
 2. Create a [twitter app](https://developer.twitter.com/en/portal/projects-and-apps). Make sure to give it **Read and Write** permissions.
 3. Set up an [Heroku account](https://www.heroku.com/)
 
## How to use

To make your own bot follow these steps:

1. Clone this repository on your local machine
2. Create a virtual environment in your project's root directory: `python3 -m venv venv && source venv/bin/activate`
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `.env` in the root directory of your project. Put your twitter App keys there:
```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<YOUR_ACCESS_TOKEN_SECRET_HERE>
CONSUMER_KEY=<YOUR_CONSUMER_KEY_HERE>
CONSUMER_SECRET=<YOUR_CONSUMER_SECRET_HERE>
```
5. Make changes in the logic of the bot by modyifing `src/twitter_bot.py`
6. Test your changes locally by running `python entrypoint.py` from the root directory of your project

## How to deploy

Once you are happy with your bot:

1. Add any additional packages you used to `requirements.txt`
2. Run `sh createlambdalayer.sh` from the root directory of your project. It'll generate a zip file with your libraries called `layer.zip`
3. Update your Lambda Layer using `layer.zip`
4. Run `sh buildpackage.sh` from the root directory of your project. It'll make a zip file with the code for your Lambda Function called `lambda_function.zip`
5. Upload `lambda_function.zip` to your Lambda Function
6. Add your twitter App keys as environment variables in the Lambda Function
7. Add a scheduled trigger to your Lambda Function using [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/run-lambda-schedule.html) 

## Limitations

Read this before using the bot:



## Attributions

*This repository was pulled as a template from Dylan Castillo: https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda to start my own Twitter bot project

