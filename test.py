import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC,ETH,LTC,XMR,DASH,NEO"

payload={}
headers = {
  'X-CMC_PRO_API_KEY': 'cd9827bb-30b7-478a-83b8-5401476cd9d1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)