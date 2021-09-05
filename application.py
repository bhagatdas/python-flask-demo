from flask import Flask
application = Flask(__name__)

@application.route('/')
def sample_method():
    return 'Hello Jagat'