import requests

response = requests.get('http://api.open-notify.org/astros.json')

data = response.json()
astronauts = data['people']

print( response.status_code )

for person in astronauts[:5]:
    print(person['name'])