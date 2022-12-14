from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, InputRequired


class WorkForm(FlaskForm):

    title = StringField('Title: ', validators=[DataRequired(message='Please enter a Title'), Length(3, 25)])

    location = StringField('Location: ')
    company_profile = StringField('Company Profile: ')
    has_company_logo = BooleanField('Company logo: ', validators=[DataRequired(message='Please confirm if you have '
                                                                                       'a logo or not')])
    employment_type = StringField('Employment type: ')
    industry = StringField('Industry: ')

    create_post = SubmitField('Upload')


class SignupForm(FlaskForm):

    email = StringField('E-mail: ', validators=[DataRequired(message='Please enter a valid Email!')])

    username = StringField('Username: ', validators=[DataRequired(message='This is required'), Length(3, 25)])
    password_hash = PasswordField('Password: ', validators=[DataRequired(), Length(3, 30)])
    repeat_pass = PasswordField('Repeat Password:', validators=[DataRequired(), EqualTo('password_hash', message="Passwords need to match")])

    create_user = SubmitField('Sign up')


class LoginForm(FlaskForm):

    username = StringField('Username: ', validators=[InputRequired()])
    password_hash = PasswordField('Password: ', validators=[InputRequired()])

    login_button = SubmitField('Login')
