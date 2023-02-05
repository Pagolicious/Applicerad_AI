from pymongo import MongoClient
from abc import ABC
from app import settings

client = MongoClient(f'mongodb://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}')
db = client[settings.DB_NAME]


# def init_db(app):
#     """
#     Set environment variables for the database in .env file in the project root
#     folder.
#     :param app: Flask app object
#     :return: None
#     """
#     global client, db
#     username = app.config["DB_USER"]
#     password = app.config["DB_PASSWORD"]
#     host = app.config["DB_HOST"]
#     port = int(app.config["DB_PORT"])
#     database = app.config["DB_NAME"]
#     client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
#     db = client[database]


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()
        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del (self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)
        else:
            return self.collection.replace_one({'_id': self._id}, self.__dict__)

    def update_with(self, new_values: dict) -> None:
        self.__dict__.update(new_values)
        self.collection.replace_one({"_id": self._id}, self.__dict__)

    def delete_field(self, field):
        self.collection.update_one({'_id': self._id}, {"$unset": {field: ""}})

    def delete(self) -> None:
        self.collection.delete_one({"_id": self._id})

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def delete_more(cls, **kwargs):
        cls.collection.delete_many(kwargs)
