import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.status_code)