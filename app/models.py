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
        return '<Run {} from user {}>'.format(self.run, self.user_id)
