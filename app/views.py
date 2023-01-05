from flask import Blueprint, render_template, url_for
from app.forms import WorkForm
from . import JobAd, db

bp_user = Blueprint(name="bp_user", import_name=__name__)


@bp_user.route('/home')
@bp_user.route('/')
def index():
    return render_template("html/index.html")


@bp_user.route('/upload/', methods=['GET', 'POST'])
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

    return render_template("html/upload.html", form=form)
