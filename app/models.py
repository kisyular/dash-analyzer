from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from datetime import datetime
from app.extensions import db
from app.extensions import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)



class ScrappedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    browser = db.Column(db.String(5000))
    time = db.Column(db.String(5000))
    unique_time = db.Column(db.String(5000))
    ip_request = db.Column(db.String(5000))
    country = db.Column(db.String(5000))
    region = db.Column(db.String(5000))
    zipcode = db.Column(db.String(5000))
    city = db.Column(db.String(5000))
    latitude = db.Column(db.String(5000))
    longitude = db.Column(db.String(5000))
    website_name = db.Column(db.String(5000))

    def __repr__(self):
        return '<Post {}>'.format(self.ip_request)



class SelectedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(5000))
    website_name = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.website_name)


class PostURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(5000))
    website_name = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.website_name)
