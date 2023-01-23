from app.persistance.repository import job_repo


def create_job(title, industry, employment_type, location, company_profile, company_logo):
    job = {
        'Title': title,
        'Industry': industry,
        'Employment Type': employment_type,
        'Location': location,
        'Company Profile': company_profile,
        'Company Logo': company_logo
    }
    job_repo.create_job(job)


def get_latest_job():
    latest = job_repo.get_all_jobs()
    return latest
