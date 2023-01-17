from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.FirstDB


def find_all_users():
    result = db.my_users.find()
    for item in result:
        print(item)


def main():
    result = db.my_users.find({'title': 'Chef'})
    for item in result:
        print(item)
    find_all_users()


if __name__ == '__main__':
    main()
