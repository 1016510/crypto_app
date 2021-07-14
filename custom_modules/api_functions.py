import requests

def get_crypto_by_abbreviation(abbreviation):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={abbreviation}"
    payload={}
    headers = {
    'X-CMC_PRO_API_KEY': 'cd9827bb-30b7-478a-83b8-5401476cd9d1'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    resp_dict = response.json()
    crypto = resp_dict['data'][abbreviation]['quote']['USD']
    return crypto
    