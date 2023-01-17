from app.persistance.models import Job


def create_job(job):
    Job(job).save()


def get_all_jobs():
    return Job.all()
