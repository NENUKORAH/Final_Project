from .app import db


class Day(db.Model):
    __tablename__ = 'daily_values'

    ticker = db.Column(db.String(10))
    hdate = db.Column(db.Date)
    hopen = db.Column(db.Float)
    hhigh = db.Column(db.Float)
    hlow = db.Column(db.Float)
    hclose = db.Column(db.Float)
    hvolume = db.Column(db.Integer)

    def __repr__(self):
        return '<Day %r>' % (self.name)
