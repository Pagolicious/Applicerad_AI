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


def main():
    job = Job('Teacher', 50000)
    job.save()


if __name__ == '__main__':
    main()
