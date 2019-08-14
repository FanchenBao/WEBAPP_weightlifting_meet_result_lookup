"""07/28/2019

Following the tutorial from 'https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/'
"""
from app import db
from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    gender = db.Column(db.String())
    rank = db.Column(db.Integer)
    rank_s = db.Column(db.Integer)
    rank_cj = db.Column(db.Integer)
    name = db.Column(db.String())
    born = db.Column(db.DateTime)
    nation = db.Column(db.String())
    weight_class = db.Column(db.String())  # need string due to super heavyweight
    bweight = db.Column(db.Float)
    snatch1 = db.Column(db.String())  # need string due to '*' mark on the misses or bomb out
    snatch2 = db.Column(db.String())
    snatch3 = db.Column(db.String())
    snatch = db.Column(db.String())
    jerk1 = db.Column(db.String())
    jerk2 = db.Column(db.String())
    jerk3 = db.Column(db.String())
    jerk = db.Column(db.String())
    total = db.Column(db.String())
    meet = db.Column(db.String())
    date = db.Column(db.DateTime)

    def __init__(self, athlete, event_id):
        self.event_id = event_id
        self.gender = athlete['gender'].lower().strip()  # unifying the representation of gender
        # Use 1000 as a marker for bombed-out ranking to avoid the '---' marker in the original data set
        self.rank = athlete['rank'].strip() if athlete['rank'].strip().isdigit() else 1000
        self.rank_s = athlete['rank_s'].strip() if athlete['rank_s'].strip().isdigit() else 1000
        self.rank_cj = athlete['rank_cj'].strip() if athlete['rank_cj'].strip().isdigit() else 1000
        self.name = athlete['name'].strip()
        self.born = datetime.strptime(athlete['born'].strip(), '%d.%m.%Y')
        self.nation = athlete['nation'].upper().strip()  # unifying the representation of nation
        self.weight_class = athlete['category'].strip()
        self.bweight = athlete['bweight'].strip()
        self.snatch1 = athlete['snatch1'].strip()
        self.snatch2 = athlete['snatch2'].strip()
        self.snatch3 = athlete['snatch3'].strip()
        self.snatch = athlete['snatch'].strip()
        self.jerk1 = athlete['jerk1'].strip()
        self.jerk2 = athlete['jerk2'].strip()
        self.jerk3 = athlete['jerk3'].strip()
        self.jerk = athlete['jerk'].strip()
        self.total = athlete['total'].strip()
        self.meet = athlete['event'].strip()
        self.date = datetime.strptime(athlete['date'].strip(), '%m.%Y')

    def __repr__(self):
        return '<id {}>'.format(self.id)
