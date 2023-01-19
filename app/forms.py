from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import Length, DataRequired, EqualTo, InputRequired, Email


class WorkForm(FlaskForm):

    title = StringField('Title: ', validators=[DataRequired(message='Please enter a Title'), Length(4, 20)])

    location = StringField('Location: ')
    company_profile = TextAreaField('Company Profile: ')
    has_company_logo = BooleanField('', validators=[DataRequired(message='Please confirm if you have '
                                                                                       'a logo or not')])
    employment_type = StringField('Employment type: ')
    industry = StringField('Industry: ')

    create_post = SubmitField('Upload')


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
