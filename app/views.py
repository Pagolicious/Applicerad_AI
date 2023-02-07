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
               collection.find({'fraudulent': {'$lt': 1}})

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
        department = form.department.data
        salary_range = form.salary_range.data
        company_profile = form.company_profile.data
        description = form.description.data
        requirements = form.requirements.data
        benefits = form.benefits.data
        telecommuting = form.telecommuting.data
        has_company_logo = form.has_company_logo.data
        has_questions = form.has_questions.data
        employment_type = form.employment_type.data
        required_experience = form.required_experience.data
        required_education = form.required_education.data
        industry = form.industry.data
        function = form.function.data

        if telecommuting:
            telecommuting = 1
        else:
            telecommuting = 0
        if has_company_logo:
            has_company_logo = 1
        else:
            has_company_logo = 0
        if has_questions:
            has_questions = 1
        else:
            has_questions = 0

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


@bp_user.route('/info/<_id>', methods=['GET', 'POST'])
def view_info(_id):
    job_object_id = job_controller.get_by_job_id(_id)
    job_id = job_object_id._id
    all_jobs = job_repo.get_all_jobs()
    if not job_id:
        abort(HTTPStatus.NOT_FOUND, "This is not the page you are looking for.")
    return render_template("html/info.html", job_id=job_id, all_jobs=all_jobs)


@bp_user.route('/update/<_id>', methods=['GET', 'POST'])
@login_required
def update(_id):
    form = WorkForm()
    job = job_controller.get_by_job_id(_id)
    job_id = job._id
    all_jobs = job_repo.get_all_jobs()

    # job.company_profile = form.company_profile.data
    # job.company_logo = form.company_logo.data
    # title = form.title.data
    # location = form.location.data

    # employment_type = form.employment_type.data
    # industry = form.industry.data
    # salary_range = form.salary_range.data
    # required_experience = form.required_experience.data
    # required_education = form.required_education.data

    if form.submit_post.data and form.validate():

        job_controller.update_by_id(_id, new_data={"title": form.title.data})
        job_controller.update_by_id(_id, new_data={"industry": form.industry.data})
        job_controller.update_by_id(_id, new_data={"employment_type": form.employment_type.data})
        job_controller.update_by_id(_id, new_data={"location": form.location.data})
        job_controller.update_by_id(_id, new_data={"company_profile": form.company_profile.data})
        job_controller.update_by_id(_id, new_data={"company_logo": form.has_company_logo.data})
        job_controller.update_by_id(_id, new_data={"salary_range": form.salary_range.data})
        job_controller.update_by_id(_id, new_data={"required_experience": form.required_experience.data})
        job_controller.update_by_id(_id, new_data={"description": form.description.data})
        job_controller.update_by_id(_id, new_data={"requirements": form.requirements.data})
        job_controller.update_by_id(_id, new_data={"benefits": form.benefits.data})
        job_controller.update_by_id(_id, new_data={"telecommuting": form.telecommuting.data})
        job_controller.update_by_id(_id, new_data={"has_questions": form.has_questions.data})
        job_controller.update_by_id(_id, new_data={"function": form.function.data})
        job_controller.update_by_id(_id, new_data={"department": form.department.data})
        job_controller.update_by_id(_id, new_data={"required_education": form.required_education.data})

        flash('Job Ad Updated Successfully!', "success")

        return redirect(url_for('bp_user.index'))

    return render_template("html/update.html", form=form, job_id=job_id, all_jobs=all_jobs, job=job)


@bp_user.route('/info/<_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(_id):
    job_controller.delete_job_by_id(_id)
    flash("Job deleted successfully.", "success")

    return redirect(url_for("bp_user.index"))
