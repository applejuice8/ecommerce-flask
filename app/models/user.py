from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.extensions import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    username = db.Column(
        db.String(100),
        nullable=False,
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )
    cart = db.relationship(
        'Cart',
        backref='user',
        uselist=False
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User id={self.id}, username={self.username} email={self.email}>'
