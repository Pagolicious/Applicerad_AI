from flask_login import UserMixin
from mongoengine import connect, Document, StringField, IntField

connect('FirstDB', username='root', password='s3cr37', authentication_source='admin')


class Job(Document):
    title = StringField(required=True)
    salary = IntField()

    meta = {
        'collection': 'jobs'
    }

    def __init__(self, title, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.salary = salary


class User(Document):
    id = IntField(primary_key=True)
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

    meta = {
        'collection': 'user'
    }

    def __init__(self, username, email, password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.email = email
        self.password = password


def main():
    job = Job('Teacher', 50000)
    job.save()

    user = User('JohanRymden', 'johan@rymden.com', 'funkardet')
    user.save()


if __name__ == '__main__':
    main()
