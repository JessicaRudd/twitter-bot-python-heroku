from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

app.run(host= '0.0.0.0', port=environ.get('PORT'))