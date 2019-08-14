"""07/28/2019

Following the tutorial from 'https://realpython.com/flask-by-example-part-1-project-setup/'
"""
import os
from flask import Flask, render_template, request, jsonify
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
    """ Query database based on user input filter. """
    results = []

    # Values to allow html keep user's previous select options or input values
    # See here https://stackoverflow.com/questions/43528644/having-a-select-option-stay-selected-after-post-with-flask
    fname = ""
    lname = ""
    gender_select = ""
    weight_class_select = ""
    nation_select = ""
    meet_select = ""

    # populate select options
    nations = sorted([v.nation.upper() for v in Result.query.with_entities(Result.nation).distinct()])
    weight_classes = sorted([v.weight_class for v in Result.query.with_entities(Result.weight_class).distinct()])
    meets = sorted([v.meet for v in Result.query.with_entities(Result.meet).distinct()])

    if request.method == 'POST':
        # Retrieve data from form submission
        fname = request.form['fname']
        lname = request.form['lname']
        gender_select = request.form['gender']
        nation_select = request.form['nation']
        weight_class_select = request.form['weight_class']
        meet_select = request.form['meet']

        # UNRELATED. To do postgresql query from command line, string must be SINGLE QUOTED
        # Refer to http://www.leeladharan.com/sqlalchemy-query-with-or-and-like-common-filters for general query syntax
        q = Result.query
        if fname:
            q = q.filter(Result.name.like('% ' + fname))
        if lname:
            q = q.filter(Result.name.like(lname + ' %'))
        if gender_select:
            q = q.filter_by(gender=gender_select)
        if nation_select:
            q = q.filter_by(nation=nation_select)
        if weight_class_select:
            q = q.filter_by(weight_class=weight_class_select)
        if meet_select:
            q = q.filter_by(meet=meet_select)
        # If no filter option is selected, do not return anything
        if fname or lname or gender_select or nation_select or weight_class_select or meet_select:
            results = q.all()
        if not results:
            results = ["No result found."]
    return render_template('index.html',
                           results=results,
                           fname=fname,
                           lname=lname,
                           weight_classes=weight_classes,
                           nations=nations,
                           meets=meets,
                           gender_select=gender_select,
                           weight_class_select=weight_class_select,
                           nation_select=nation_select,
                           meet_select=meet_select)


@app.route('/weight_class')
def get_weight_class():
    """ Dynamically update weight class options based on gender input """
    gender = request.args.get('gender')
    q = Result.query.with_entities(Result.weight_class).filter_by(gender=gender).distinct()
    weight_classes = sorted(v.weight_class for v in q)
    return jsonify(weight_classes)


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
