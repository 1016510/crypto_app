from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

app = Flask(__name__)
app.secret_key=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,'database.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models