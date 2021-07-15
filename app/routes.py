from flask import render_template, request
from app.custom_modules.api_functions import get_crypto_by_abbreviation

import os
import sqlite3
import pandas as pd
from datetime import datetime
from app import app, db
from app.models import Crypto
from app.forms import CryptoForm




@app.route('/', methods=['POST','GET'])
def show_crypto():
    # database verbinding aanmaken, maakt de database aan als deze niet bestaat
    con = sqlite3.connect('cur_database.db')
    cursor = con.cursor()
    
    # maakt de noodzakelijke tabel aan als deze nog niet bestaat
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS currency_tabel 
            (currency text)
            ''')
    con.commit()

    

    # we maken een currency lijst aan die we aan een tabel toevoegen in de database
    # we kunnen als we tijd over hebben iets maken dat we er een currency aan toe kunnen voegen
    currencies_list = ['BTC', 'ETH']
    currency_df = pd.DataFrame(currencies_list, columns=['currency'])
    currency_df.to_sql('currency_tabel', con, if_exists='replace')
    
    # fetch de currencies uit de database voor de dropdown menu op de pagina

    qry = '''SELECT currency 
             FROM currency_tabel
          '''
    
    currency_df_voor_currencylist = pd.read_sql(qry, con)
    
    # van de opgehaalde dataframe maken we van de kolom currency een list
    currencylist = currency_df_voor_currencylist['currency'].to_list()

    # raise ValueError()
  
    if request.method == 'POST':
        currency = request.form.get('currency').upper()
        quantity = request.form.get('quantity')


        crypto = get_crypto_by_abbreviation(currency)
        amount = float(quantity) * crypto['price']
        

        form = CryptoForm()
        new_currency = Crypto(zaaknaam = form.zaaknummer.data,
                              verdachte = form.verdachte.data,
                              currency  = form.currency.data,
                              aantal  = form.quantity.data,
                              datum_tijd = str(datetime.now()),
                              totale_waarde    = amount)
        
        db.session.add(new_currency)
        db.session.commit()

        return render_template('show_crypto.html', crypto=crypto, amount=amount, currencylist=currencylist)

        

    else:
        return render_template('show_crypto.html', currencylist=currencylist)

