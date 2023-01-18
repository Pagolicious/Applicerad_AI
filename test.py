from app.controller.job_controller import create_job
from app.controller.user_controller import create_user


def main():
    title = input('Title: ')
    salary = input('Salary: ')
    create_job(title, salary)

def user():
    username = input('username: ')
    email = input('email: ')
    password = input('password: ')
    create_user(username, email, password)


if __name__ == '__main__':
    main()
    # user()
