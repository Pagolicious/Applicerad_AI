from app.controller.job_controller import create_job
from app.controller.user_controller import create_user
from app.controller.job_controller import get_latest_job


def main():
    title = input('Title: ')
    salary = input('Salary: ')
    create_job(title, salary)

def user():
    username = input('username: ')
    email = input('email: ')
    password = input('password: ')
    create_user(username, email, password)

def get_last_job():
    latest = get_latest_job()
    print(latest)


if __name__ == '__main__':
    # main()
    # user()
    get_last_job()
