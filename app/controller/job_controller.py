from app.persistance.repository import job_repo


def create_job(title, location, department, salary_range, company_profile, description, requirements, benefits,
               telecommuting, has_company_logo, has_questions, employment_type, required_experience, required_education,
               industry, function, fraudulent=None):
    job = dict(
        title=title,
        location=location,
        department=department,
        salary_range=salary_range,
        company_profile=company_profile,
        description=description,
        requirements=requirements,
        benefits=benefits,
        telecommuting=telecommuting,
        has_company_logo=has_company_logo,
        has_questions=has_questions,
        employment_type=employment_type,
        required_experience=required_experience,
        required_education=required_education,
        industry=industry,
        function=function,
        fraudulent=fraudulent
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
