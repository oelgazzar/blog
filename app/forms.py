from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads
from . import app

# flask_uploads
images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class AuthForm(Form):
    username = StringField(
        'USERNAME', validators=[
            DataRequired('DataRequired')])
    password = PasswordField(
        'PASSWORD', validators=[
            DataRequired()])


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])
    image = FileField(
        'image', validators=[
            FileRequired(), FileAllowed(
                images, 'Images Only')])
