from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    map_drops = db.relationship('MapDrop', backref='player', lazy='dynamic')
    treasure_drops = db.relationship('TreasureDrop', backref='player', lazy='dynamic')

    def __repr__(self):
        return '<User {} reporting>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class MapDrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map = db.Column(db.Integer)
    gold_map = db.Column(db.Integer)
    rouge = db.Column(db.Integer)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    run = db.Column(db.Integer)

    def __repr__(self):
        return '<Run {} from {}: ({}, {}. {})>'.format(self.run, self.player.username, 
                                                        self.map, self.gold_map, self.rouge)

class ItemDrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_count = db.Column(db.Integer)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))

    def __repr__(self):
        return '<Item {} x{} from quest {}>'.format(self.item_name, self.item_count, self.quest_id)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    item_drops = db.relationship('ItemDrop', backref='quest', lazy='dynamic')

    def __repr__(self):
        return '<Quest {}: {}>'.format(self.id, self.name)

class TreasureDrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    drop1 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop2 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop3 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop4 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop5 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop6 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop7 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop8 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop9 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))
    drop10 = db.Column(db.Integer, db.ForeignKey('item_drop.id'))

    def __repr__(self):
        return '<Quest {} drop by user {}>'.format(self.quest_id, self.user_id)
