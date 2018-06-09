# imports
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

# DataBase instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# flask-login configuration
login = LoginManager(app)
login.login_view = 'auth.login'
login.init_app(app)

# register the Blueprints occur here
from . import auth
app.register_blueprint(auth.bp)

from . import models, routes
