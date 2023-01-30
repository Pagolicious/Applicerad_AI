from app.persistance.repository import job_repo


def create_job(title, industry, employment_type, location, company_profile, company_logo, salary_range,
               required_experience, required_education, fraudulent=None):
    job = dict(
        title=title,
        industry=industry,
        employment_type=employment_type,
        location=location,
        company_profile=company_profile,
        company_logo=company_logo,
        salary_range=salary_range,
        required_experience=required_experience,
        required_education=required_education,
        fradulent=fraudulent
    )

    job_repo.create_job(job)


def get_by_job_id(_id):
    return job_repo.get_by_id(_id)


def get_all_jobs():
    all_jobs = job_repo.get_all_jobs()
    return all_jobs


def get_latest_job():
    latest_job = job_repo.get_latest_job()
    return latest_job
