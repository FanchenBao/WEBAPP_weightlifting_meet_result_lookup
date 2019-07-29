"""07/28/2019

Following the tutorial from 'https://realpython.com/flask-by-example-part-1-project-setup/'
"""
import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result  # this line is important. Otherwise, migration would fail


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/import_all')
def import_csv():
    """
    '/import_all' url should only be called ONCE to initialize the database. The initial plan to populate the database
    with data from a csv file will not work properly, because after local database is populated, it must then be
    imported into the database on heroku, which will be extra hassle. Therefore, it is necessary to scrape the result
    info again, but with request and beautifulsoup, since scrapy won't be useful here.
    """
    pass


if __name__ == '__main__':
    app.run()
