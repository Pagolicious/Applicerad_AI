from bson import ObjectId

from app.persistance.db import ResultList
from app.persistance.models import Job


def create_job(job):
    Job(job).save()


def get_all_jobs():
    return Job.all()


def get_latest_job():
    return Job.find().last_or_none()


def get_by_id(_id):
    # return ResultList(Job(i) for i in Job.collection.find(dict(_id=_id))).first_or_none()
    try:
        return Job(Job.collection.find_one(dict(_id=ObjectId(_id))))
    except TypeError:
        return None


def update_by_id(_id, new_data):
    job = get_by_id(_id)
    job.update_with(new_data)


def delete_job_by_id(_id):
    job = get_by_id(_id)
    job.delete()
