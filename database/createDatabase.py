from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create the Flask application and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)