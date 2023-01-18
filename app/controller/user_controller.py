from app.persistance.repository import user_repo
from werkzeug.security import generate_password_hash


def create_user(username, email, password):
    user = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password),
        }
    user_repo.create_user(user)
