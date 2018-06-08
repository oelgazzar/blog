from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask application instance
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# register the Blueprints occur here
from . import auth
app.register_blueprint(auth.bp)

# DataBase instance

from . import models, routes
