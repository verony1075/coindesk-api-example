import requests
import os
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
print(r.json())

def extract_track_id(url):
    return url.split('/')[-1].split('?')[0]

track_url = input("Enter a Spotify track URL: ")
track_id = extract_track_id(track_url)


r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

#https://open.spotify.com/track/3QJsSWa0Xo8MfaRn1gr4Be
# import os
# CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
# CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
# auth_response = requests.post(AUTH_URL, {
# 'grant_type': 'client_credentials',
# 'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
# 'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
# })