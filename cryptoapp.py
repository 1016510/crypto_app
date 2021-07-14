from flask import Flask, render_template, request
from custom_modules.api_functions import get_crypto_by_abbreviation

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def show_crypto():
    if request.method == 'POST':
        currency = request.form.get('brand').upper()
        quantity = request.form.get('quantity')


        crypto = get_crypto_by_abbreviation(currency)
        amount = float(quantity) * crypto['price']
        return render_template('show_crypto.html', crypto=crypto, amount=amount)

    else:
        return render_template('show_crypto.html')

if __name__ == '__main__':
    app.run()