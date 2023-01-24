from bson import ObjectId

from app.persistance.db import ResultList
from app.persistance.models import Job


def create_job(job):
    Job(job).save()


def get_all_jobs():
    return Job.all()


def get_by_id(_id):
    return ResultList(Job(i) for i in Job.collection.find(dict(_id=_id))).first_or_none()

