from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired


class AuthForm(Form):
    username = StringField(
        'USERNAME', validators=[
            DataRequired('DataRequired'), InputRequired(
                message='please choose your username')])
    password = PasswordField(
        'PASSWORD', validators=[
            DataRequired(), InputRequired(
                message='please write strong password')])
