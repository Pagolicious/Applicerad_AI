from app.persistance.db import Document, db


class Job(Document):
    collection = db.jobs


class User(Document):
    collection = db.users

    #def get_id(self):
       # return self.
