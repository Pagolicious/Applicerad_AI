from MongoDB_no_flask.mongo_base_model import ResultList
from app.persistance.models import User

def create_user(user):
    User(user).save()


def get_all_users():
    return User.all()

def get_by_username(username):
    return ResultList(User(i) for i in User.collection.find(dict(username=username))).first_or_none()

def check_existing_users(username, email):

    if User.collection.find_one({"username": username}) is not None:
        print(f"{username} already exists in database")
        return False

    if User.collection.find_one({"email": email}) is not None:
        print(f"{email} already exists in database")
        return False
    return True
