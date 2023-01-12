from flask import Blueprint, render_template, url_for, current_app, flash, redirect, request
from flask_login import login_user, login_required
# from itsdangerous import URLSafeTimedSerializer

from app.forms import WorkForm, SignupForm, LoginForm
from . import db, User
# from .repo import check_existing_users, create_user
from werkzeug.security import generate_password_hash, check_password_hash

bp_user = Blueprint(name="bp_user", import_name=__name__)


@bp_user.route('/home')
@bp_user.route('/')
def index():
    return render_template("html/index.html")


@bp_user.route('/upload/', methods=['GET', 'POST'])
# @login_required
def upload():
    form = WorkForm()
    if form.validate_on_submit():

        post = Post(title=form.title.data,
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
        # username = request.form.get('username')
        # email = request.form.get('email')
        # password_hash = request.form.get('password_hash')
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
        # username = form.username.data
        # email = form.email.data
        # password_hash = form.password_hash.data
        # user = Users.query.filter_by(email=form.email.data).first()
        # if user is None:
            # hashed_pw = generate_password_hash(form.password_hash.data, "djke248")
            user = User(username=form.username.data, email=form.email.data, password_hash=form.password_hash.data)
            db.session.add(user)
            db.session.commit()
            flash("User Added Successfully")

        # if check_existing_users(username, email):
        #     create_user(email, username, password_hash)
        else:
            flash('Username Already Exists')
    all_users = User.query.order_by(User.username)
        # username = form.username.data
        # form.username.data = ''
        # form.email.data = ''
        # form.password_hash.data = ''
        # token = serializer.dumps(email)
        # return redirect("html/login.html", username=username, form=form)

    return render_template("html/signup.html", username=username, form=form, all_users=all_users)

@bp_user.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

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


@bp_user.route('/delete/<int:id>')
def delete(id):
    # username = None
    # form = SignupForm()
    delete_user = User.query.get_or_404(id)
    try:
        db.session.delete(delete_user)
        db.session.commit()
        flash('User has been deleted!')
        all_users = User.query.order_by(User.username)
        return render_template("html/index.html", all_users=all_users)

    except:
        flash("Didn't delete anything")
