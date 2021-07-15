from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, TextField


class CryptoForm(FlaskForm):
    zaaknummer  = TextField("zaaknummer")
    verdachte   = TextField("verdachte")
    currency    = TextField("currency")
    quantity    = FloatField("quantity")
    submit      = SubmitField("verstuur")
    