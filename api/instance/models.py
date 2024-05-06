import sys
sys.path.append('../')

from core import *

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<profiles %r>' % self.id