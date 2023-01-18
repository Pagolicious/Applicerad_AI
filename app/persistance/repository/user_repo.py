from app.persistance.models import User


def create_user(user):
    User(user).save()


def get_all_users():
    return User.all()
