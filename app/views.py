from http import HTTPStatus

from flask import Blueprint, render_template, url_for, current_app, flash, redirect, request, abort
from flask_login import login_user, login_required, logout_user, current_user
from app.controller import job_controller
from RandomForest import predict

from app.forms import WorkForm, SignupForm, LoginForm
from .controller import user_controller

from werkzeug.security import generate_password_hash, check_password_hash

from .persistance.models import Job
from .persistance.repository import job_repo

bp_user = Blueprint(name="bp_user", import_name=__name__)
collection = Job.collection


@bp_user.route('/home', methods=['GET', 'POST'])
@bp_user.route('/', methods=['GET', 'POST'])
def index():
    all_jobs = job_repo.get_all_jobs() and \
               collection.find({'fradulent': {'$lt': 1}})

    return render_template("html/index.html", all_jobs=all_jobs)


@bp_user.route("/signup/", methods=['GET', 'POST'])
def signup():
    username = None
    form = SignupForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        email = form.email.data

        if user_controller.check_existing_users(username, email):

            user_controller.create_user(email, username, password)
            flash(f"Account Created Successfully!", "success")
            print("User Added Successfully")

        else:
            flash('Username or Email Already Exists', "error")
            print('Username Already Exists')

    return render_template("html/signup.html", username=username, form=form)


@bp_user.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = user_controller.get_by_username(username)

        if user is not None:
            if check_password_hash(user.password, password):
                login_user(user)
                flash(f"{user.username} Logged in", "success")

                return redirect(url_for("bp_user.index", username=user.username))

            else:
                flash('Invalid Credentials', "error")
                print('Invalid1')

        else:
            flash('Invalid Credentials', "error")
            print('Invalid2')

    return render_template("html/login.html", form=form)


@bp_user.get("/logout")
@login_required
def logout():
    logout_user()
    flash("You Logged Out", "success")

    return redirect(url_for("bp_user.index"))


@bp_user.route('/upload/', methods=['GET', 'POST'])
@login_required
def upload():
    form = WorkForm()
    if form.validate_on_submit():
        title = form.title.data
        location = form.location.data
        department = None
        salary_range = form.salary_range.data
        company_profile = form.company_profile.data
        description = None
        requirements = None
        benefits = None
        telecommuting = None
        has_company_logo = form.has_company_logo.data
        has_questions = None
        employment_type = form.employment_type.data
        required_experience = form.required_experience.data
        required_education = form.required_education.data
        industry = form.industry.data
        function = None

        print("Predicting job")
        fraudulent = predict.prediction(title, location, department, salary_range, company_profile, description,
                                        requirements, benefits, telecommuting, has_company_logo, has_questions,
                                        employment_type, required_experience, required_education, industry, function,)
        job_controller.create_job(title, location, department, salary_range, company_profile, description, requirements,
                                  benefits, telecommuting, has_company_logo, has_questions, employment_type,
                                  required_experience, required_education, industry, function, fraudulent)
        flash("Posted Job Ad Successfully", "success")
        print(job_controller.get_latest_job())
        return redirect(url_for("bp_user.index"))


    return render_template("html/upload.html", form=form)


@bp_user.route('/info/<title>', methods=['GET', 'POST'])
def view_info(title):
    # job = job_controller.get_by_job_id(_id)
    all_jobs = job_repo.get_all_jobs()
    if not title:
        abort(HTTPStatus.NOT_FOUND, "This is not the page you are looking for.")
    return render_template("html/info.html", job_title=title, all_jobs=all_jobs)
