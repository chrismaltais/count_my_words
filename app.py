import os
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

# Both GET and POST because we route to the same palce for both requests
@app.route('/', methods = ['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # Get the URL the user has entered
        try:
            url = request.form['url']
            r = requests.get(url)
            print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, results=results)

#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}".format(name)

if __name__ == '__main__':
    app.run()