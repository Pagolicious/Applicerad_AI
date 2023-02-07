from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import Length, DataRequired, EqualTo, InputRequired, Email
from wtforms.widgets import TextArea

from app.controller import job_controller


class WorkForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired(message='Please enter a Title'), Length(4, 200)])

    location = StringField('Location: ')
    company_profile = TextAreaField('Company Profile: ')
    has_company_logo = BooleanField('')
    employment_type = StringField('Employment type: ')
    industry = StringField('Industry: ')
    salary_range = StringField('Salary Range: ', render_kw={"placeholder": "### - ###"})
    required_experience = StringField('Required Experience: ')
    required_education = StringField('Required Education: ')
    department = StringField('Department: ')
    description = TextAreaField('Description: ')
    requirements = StringField('Requirements: ')
    benefits = StringField('Benefits: ')
    telecommuting = BooleanField('')
    has_questions = BooleanField('')
    function = StringField('Function: ')

    submit_post = SubmitField('Submit')


class SignupForm(FlaskForm):

    email = StringField('E-mail: ', validators=[DataRequired(message='Please enter a valid Email!'),
                                                Email(message='Please enter a valid Email')],
                                                render_kw={"placeholder": "example@example.com"})

    username = StringField('Username: ', validators=[DataRequired(message='This is required'), Length(3, 25)])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(3, 30)])
    repeat_pass = PasswordField('Repeat Password:', validators=[DataRequired(), EqualTo('password', message="Passwords need to match")])

    create_user = SubmitField('Sign up')


class LoginForm(FlaskForm):

    username = StringField('Username: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired()])

    login_button = SubmitField('Login')


# class UpdateForm(FlaskForm):
#
#     title = StringField('Title: ', validators=[DataRequired(message='Please enter a Title'), Length(4, 200)])
#
#     location = StringField('Location: ')
#     company_profile = TextAreaField('Company Profile: ')
#     has_company_logo = BooleanField('')
#     employment_type = StringField('Employment type: ')
#     industry = StringField('Industry: ')
#     salary_range = StringField('Salary Range: ', render_kw={"placeholder": "### - ### Hourly/Monthly/Yearly"})
#     required_experience = StringField('Required Experience ')
#     required_education = StringField('Required Education ')
#     department = StringField('Department ')
#     description = TextAreaField('Description ')
#     requirements = StringField('Requirements ')
#     benefits = StringField('Benefits ')
#     telecommuting = StringField('Telecommuting ')
#     has_questions = StringField('Questions ')
#
#     update_post = SubmitField('Update')
