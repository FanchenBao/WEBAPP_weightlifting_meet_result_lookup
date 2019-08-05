"""07/28/2019

Following the tutorial from 'https://realpython.com/flask-by-example-part-1-project-setup/'
"""
import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from web_scrape import WebScrape
import re

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result  # this line is important. Otherwise, migration would fail


def import_weightlifting_data(base_url, start_url, start_year, end_year):
    """ Scrape iwf official website to import meet results in a given year range.
        Note that the year range for old body weight category is 1998 to 2018,
        for new body weight 2018 to present
    """
    ws = WebScrape(base_url, start_url)
    for year in range(start_year, end_year + 1):
        event_urls = ws.scrape_year(year)  # get all urls for events
        for event_url in event_urls:
            m = re.search(r'event=(\d+)', event_url)
            event_id = m.group(1)  # get event_id. It is used to identify whether an event has been recorded already
            result_url = ws.scrape_event(event_url)  # get url to event result from event url
            all_athletes = ws.output(result_url)  # output results of all athletes
            for athlete in all_athletes:
                res = Result(athlete, event_id)
                db.session.add(res)  # push into db
                db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/import_all')
def import_all():
    """
    '/import_all' url should only be called ONCE to initialize the database. The initial plan to populate the database
    with data from a csv file will not work properly, because after local database is populated, it must then be
    imported into the database on heroku, which will be extra hassle. Therefore, it is necessary to scrape the result
    info again, but with request and beautifulsoup, since scrapy won't be useful here.
    """
    base_url = 'https://www.iwf.net'
    old_bw_start_url = '/results/results-by-events/?event_year='  # duration 1998 - 2018
    new_bw_start_url = '/new_bw/results_by_events/?event_year='  # duration 2018 - present

    table_exists = Result.query.limit(1).all()
    if table_exists:  # check whether the database has already been populated
        error = "ERROOR: Database already populated."
    else:
        try:
            # import old body weight
            import_weightlifting_data(base_url, old_bw_start_url, 1998, 2018)
            # import new body weight
            import_weightlifting_data(base_url, new_bw_start_url, 2018, 2019)
            error = "Success"
        except:
            error = 'ERROR: Import failed'
    return render_template('import_outcome.html', error=error)


if __name__ == '__main__':
    app.run()
