# import requests

# url = 'https://httpbin.org/post'
# response = requests.post(url)

# print(response.json())

import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.status_code)