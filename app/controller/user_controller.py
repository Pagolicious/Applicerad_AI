from app.persistance.models import User
from app.persistance.repository import user_repo
from werkzeug.security import generate_password_hash


def create_user(email, username, password):
    # user = {
    #         'username': username,
    #         'email': email,
    #         'password': generate_password_hash(password),
    #     }

    user = dict(
        email=email,
        username=username,
        password=generate_password_hash(password)
    )

    if check_existing_users(username, email):
        user_repo.create_user(user)

def get_by_username(username):
    return user_repo.get_by_username(username)

def check_existing_users(username, email):
    return user_repo.check_existing_users(username, email)
