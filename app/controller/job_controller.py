from app.persistance.repository import job_repo


def create_job(title, industry, employment_type, location, company_profile, company_logo, salary_range,
               required_experience, required_education):
    job = dict(
        title=title,
        industry=industry,
        employment_type=employment_type,
        location=location,
        company_profile=company_profile,
        company_logo=company_logo,
        salary_range=salary_range,
        required_experience=required_experience,
        required_education=required_education
    )

    job_repo.create_job(job)


def get_by_job_id(_id):
    return job_repo.get_by_id(_id)

