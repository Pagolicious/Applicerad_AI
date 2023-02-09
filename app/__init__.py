from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    _app = Flask(__name__)
    _app.config['SECRET_KEY'] = "very secret"

    _app.config.from_pyfile('settings.py')

    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(username):
        from app.controller.user_controller import get_by_username
        return get_by_username(username)

    from.views import bp_user
    _app.register_blueprint(bp_user, url_prefix='/')

    return _app
