from flask import Flask
from os import path
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database.db"
db = SQLAlchemy()


class JobAd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    location = db.Column(db.String(100))
    company_profile = db.Column(db.String(1000))
    has_company_logo = db.Column(db.Boolean())
    employment_type = db.Column(db.String(100))
    industry = db.Column(db.String(100))
    is_posted_since = db.Column(db.DateTime, default=datetime)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = "very secret"

    db.init_app(app)

    from.views import bp_user
    app.register_blueprint(bp_user, url_prefix='/')

    if not path.exists('Applicerad_AI/' + DB_NAME):
        with app.app_context():
            db.create_all()

    return app

