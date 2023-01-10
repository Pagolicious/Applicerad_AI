from flask import Blueprint, render_template, url_for, current_app, flash, redirect
from flask_login import login_user, login_required
# from itsdangerous import URLSafeTimedSerializer

from app.forms import WorkForm, SignupForm, LoginForm
from . import JobAd, db, Users
from werkzeug.security import generate_password_hash, check_password_hash

bp_user = Blueprint(name="bp_user", import_name=__name__)


@bp_user.route('/home')
@bp_user.route('/')
def index():
    return render_template("html/index.html")


@bp_user.route('/upload/', methods=['GET', 'POST'])
@login_required
def upload():
    form = WorkForm()
    if form.validate_on_submit():

        post = JobAd(title=form.title.data,
                     location=form.location.data,
                     company_profile=form.company_profile.data,
                     has_company_logo=form.has_company_logo.data,
                     employment_type=form.employment_type,
                     industry=form.industry.data)

        form.title.data = ''
        form.location.data = ''
        form.company_profile.data = ''
        form.has_company_logo.data = ''
        form.employment_type.data = ''
        form.industry.data = ''

        db.session.add(post)
        db.session.commit()
        flash("Posted Job Ad Successfully")

    return render_template("html/upload.html", form=form)


@bp_user.route("/signup/", methods=['GET', 'POST'])
def signup():
    username = None
    form = SignupForm()
    # serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            hashed_pw = generate_password_hash(form.password_hash.data, "djke248")
            user = Users(username=form.username.data, email=form.email.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        else:
            flash('Username Already Exists')
        username = form.username.data
        form.username.data = ''
        form.email.data = ''
        form.password_hash.data = ''
        flash("User Added Successfully")
        # token = serializer.dumps(email)

    return render_template("html/signup.html", username=username, form=form)

@bp_user.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()

        if user is not None:
            if check_password_hash(user.passowrd_hash, form.password_hash.data):
                # if user.is_confirmed:
                login_user(user)
                flash(user.email)
                flash(user.username)

                return redirect(url_for("html.upload"))
                # else:
                #
                #     return redirect(url_for("auth.not_verified", username=user.username))
            else:
                flash('Invalid Credentials')

        else:
            flash('Invalid Credentials')

    return render_template("html/login.html", form=form)
