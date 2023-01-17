from app.persistance.db import Document, db


class Job(Document):
    collection = db.jobs
