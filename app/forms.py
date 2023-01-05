from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired


class WorkForm(FlaskForm):

    title = StringField('Title: ', validators=[DataRequired(message='Please enter a Title'), Length(3, 25)])

    location = StringField('Location: ')
    company_profile = StringField('Company Profile: ')
    has_company_logo = BooleanField('Company logo: ', validators=[DataRequired(message='Please confirm if you have '
                                                                                       'a logo or not')])
    employment_type = StringField('Employment type: ')
    industry = StringField('Industry: ')

    create_post = SubmitField('Upload')
