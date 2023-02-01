from app.controller.job_controller import create_job
from app.controller.user_controller import create_user
from app.controller.job_controller import get_latest_job


def main():
    title = input('Title: ')
    industry = input('industry: ')
    employment_type = input('employment_type: ')
    location = input('location: ')
    company_profile = input('company_profile: ')
    company_logo = input('company_logo: ')
    salary_range = input('salary_range: ')
    required_experience = input('required_experience: ')
    required_education = input('required_education: ')
    create_job(title, industry, employment_type, location, company_profile, company_logo,
               salary_range, required_experience, required_education)

def user():
    username = input('username: ')
    email = input('email: ')
    password = input('password: ')
    create_user(username, email, password)

def get_last_job():
    latest = get_latest_job()
    print(latest)


if __name__ == '__main__':
    main()
    # user()
    #get_last_job()
