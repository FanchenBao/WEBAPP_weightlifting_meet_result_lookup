"""07/28/2019

Following the tutorial from 'https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/'
"""
from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String())
    rank = db.Column(db.Integer)
    rank_s = db.Column(db.Integer)
    rank_cj = db.Column(db.Integer)
    name = db.Column(db.String())
    born = db.Column(db.DateTime)
    nation = db.Column(db.String())
    category = db.Column(db.String())  # need string due to super heavyweight
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
    event = db.Column(db.String())
    date = db.Column(db.DateTime)

    def __init__(self, athlete):
        self.gender = athlete.gender
        self.rank = athlete.rank
        self.rank_s = athlete.rank_s
        self.rank_cj = athlete.rank_cj
        self.name = athlete.name
        self.born = athlete.born
        self.nation = athlete.nation
        self.category = athlete.category
        self.bweight = athlete.bweight
        self.snatch1 = athlete.snatch1
        self.snatch2 = athlete.snatch2
        self.snatch3 = athlete.snatch3
        self.snatch = athlete.snatch
        self.jerk1 = athlete.jerk1
        self.jerk2 = athlete.jerk2
        self.jerk3 = athlete.jerk3
        self.jerk = athlete.jerk
        self.total = athlete.total
        self.event = athlete.event
        self.date = athlete.date

    def __repr__(self):
        return '<id {}>'.format(self.id)
