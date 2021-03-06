# imports
from datetime import datetime
from app import db, login
from flask_login import UserMixin


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    filename = db.Column(db.String, nullable=True)
    file_url = db.Column(db.String, nullable=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def date(self):
        return self.pub_date.strftime('%d %B - %I:%M %P')

    def __repr__(self):
        return '<Post %r>' % self.title


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    time_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '{}'.format(self.username)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default='Anonymous')
    body = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def date(self):
        return self.timestamp.strftime('%d %B - %I:%M %P')

    def __repr__(self):
        return '<Comment %r>' % self.body


@login.user_loader
def load_user(id):
    """
    loads the user using the corresponding id
    """

    return User.query.get(int(id))
