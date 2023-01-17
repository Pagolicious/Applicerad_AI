from app.persistance.repository import job_repo


def create_job(title, salary):
    job = {
        'title': title,
        'salary': salary
    }
    job_repo.create_job(job)
