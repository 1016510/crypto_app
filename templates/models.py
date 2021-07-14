from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

##### Models
class Crypto(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    zaaknaam      = db.Column(db.String(64))
    verdachte     = db.Column(db.String(64))
    currency      = db.Column(db.String(64))
    aantal        = db.Column(db.Float)
    totale_waarde = db.Column(db.Float)
    datum_tijd    = db.Coumns(db.T)