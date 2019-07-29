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

    def __init__(self, gender, rank, rank_s, rank_cj, name, born, nation, category, bweight, snatch1, snatch2, snatch3, snatch, jerk1, jerk2, jerk3, jerk, total, event, date):
        self.gender = gender
        self.rank = rank
        self.rank_s = rank_s
        self.rank_cj = rank_cj
        self.name = name
        self.born = born
        self.nation = nation
        self.category = category
        self.bweight = bweight
        self.snatch1 = snatch1
        self.snatch2 = snatch2
        self.snatch3 = snatch3
        self.snatch = snatch
        self.jerk1 = jerk1
        self.jerk2 = jerk2
        self.jerk3 = jerk3
        self.jerk = jerk
        self.total = total
        self.event = event
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
