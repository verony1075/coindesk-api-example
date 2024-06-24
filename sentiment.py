import requests
somevalue = input()
url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': somevalue}
response = requests.post(url, data = myobj)
print(response.json())






