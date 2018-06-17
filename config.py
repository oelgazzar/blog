import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOADS_DEFAULT_DEST = basedir + '/app/static/upload/'
    # UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/upload/'

    UPLOADED_IMAGES_DEST = basedir + '/app/static/upload/'
    # UPLOADED_IMAGES_URL = 'http://localhost:5000/static/upload/'
