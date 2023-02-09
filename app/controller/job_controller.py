from flask_login import current_user

from app.persistance.repository import job_repo


def create_job(title, location, department, salary_range, company_profile, description, requirements, benefits,
               telecommuting, has_company_logo, has_questions, employment_type, required_experience, required_education,
               industry, function, fraudulent):
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
        fraudulent=fraudulent,
        created_by=current_user.username
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


def update_by_id(_id, new_data):
    return job_repo.update_by_id(_id, new_data)


def delete_job_by_id(_id):
    return job_repo.delete_job_by_id(_id)
