from flask import Flask
from os import path
from datetime import datetime
from pymongo.collection import Collection


from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

DB_NAME = "database.db"
db = SQLAlchemy()
login_manager = LoginManager()


# class Post(db.Model):
#     post_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     location = db.Column(db.String(100))
#     company_profile = db.Column(db.String(1000))
#     has_company_logo = db.Column(db.Boolean())
#     employment_type = db.Column(db.String(100))
#     industry = db.Column(db.String(100))
#     is_posted_since = db.Column(db.DateTime, default=datetime)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    # account_added = db.Column(db.DateTime, default=datetime)
    password_hash = db.Column(db.String(100))
    # posts = db.relationship('Post')

    # def __init__(self, id, username, email, password_hash):
    #     self.id = id
    #     self.username = username
    #     self.email = email
    #     self.password_hash = password_hash

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute! ')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Name %r>' % self.name

    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #     return self.username


# class User:
#     collection: Collection = db.users
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.username




def create_app():
    _app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    _app.config['SECRET_KEY'] = "very secret"
    from app import settings
    _app.config.from_pyfile('settings.py')
    # db.init_app(app)
    from app.persistance.db import init_db
    init_db(_app)

    from.views import bp_user
    _app.register_blueprint(bp_user, url_prefix='/')

    # if not path.exists('Applicerad_AI/' + DB_NAME):
    #     with _app.app_context():
    #         db.create_all()
    from app.persistance.db import db
    print(db, 'what is db')
    return _app

def initialize_extensions(app):
    login_manager.init_app(app)
    login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))