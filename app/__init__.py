from flask import Flask
from flask_login import UserMixin, LoginManager

# from app.controller import user_controller

login_manager = LoginManager()

def create_app():
    _app = Flask(__name__)
    _app.config['SECRET_KEY'] = "very secret"

    _app.config.from_pyfile('settings.py')

    # from app.persistance.db import init_db
    # init_db(_app)

    # initialize_extensions(_app)
    login_manager = LoginManager()
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(username):
        from app.controller.user_controller import get_by_username
        return get_by_username(username)

    from.views import bp_user
    _app.register_blueprint(bp_user, url_prefix='/')

    return _app

# def initialize_extensions(_app):
#     login_manager.init_app(_app)
#     login_manager.login_view = 'login'
# #
# @login_manager.user_loader
# def load_user(username):
#     return user_controller.get_by_username(username)
