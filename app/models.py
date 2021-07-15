import os
from app import db

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.secret_key=os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI']='database.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


##### Models
class Crypto(db.Model):
    __tablename__ = 'cryptozaken'
    id            = db.Column(db.Integer, primary_key=True)
    zaaknaam      = db.Column(db.String(64))
    verdachte     = db.Column(db.String(64))
    currency      = db.Column(db.String(64))
    aantal        = db.Column(db.Float)
    totale_waarde = db.Column(db.Float)
    datum_tijd    = db.Column(db.String(64))