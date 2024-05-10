import sys
sys.path.append('../')

from core import *

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<profiles %r>' % self.id
    
class Heroes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    klas = db.Column(db.String(256), nullable=False)
    can_spell = db.Column(db.Integer, nullable=False, default=0)
    race = db.Column(db.String(256), nullable=False)
    variant = db.Column(db.String(256), nullable=False)
    lvl = db.Column(db.Integer, nullable=False, default=1)
    exp = db.Column(db.Integer, nullable=False, default=0)
    count_mana = db.Column(db.String(256), nullable=False, default=0) #если несколько, то тут значения через запятую

    def __repr__(self):
        return '<profiles %r>' % self.id
    
class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    klas = db.Column(db.String(256), nullable=False)
    variant = db.Column(db.String(256), nullable=False)
    short_disc = db.Column(db.String(256), nullable=False)
    disc = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    lvl_mana = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return '<profiles %r>' % self.id
    
class KlassData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    klas = db.Column(db.String(256), nullable=False)
    lvl = db.Column(db.Integer, nullable=False)
    max_spell = db.Column(db.Integer, nullable=False)
    max_mana = db.Column(db.String(256), nullable=False) #если несколько, то тут значения через запятую
    name_mana = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<profiles %r>' % self.id
    
class VariantData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variant = db.Column(db.String(256), nullable=False)
    klas = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<profiles %r>' % self.id
    
class HeroesSpell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero = db.Column(db.Integer, nullable=False)
    spell = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<profiles %r>' % self.id