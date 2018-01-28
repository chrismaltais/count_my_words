import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

# Both GET and POST because we route to the same palce for both requests
@app.route('/', methods = ['GET', 'POST'])
def hello():
    return render_template('index.html')

#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}".format(name)

if __name__ == '__main__':
    app.run()