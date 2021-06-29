import requests
import spotipy

url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'Special Agent', 'body': 'Leroy Jethro Gibbs', 'userId': 1}

response = requests.post(url, data)

print(response.status_code)
print(response.json())

CLIENT_ID = '19c1eccd1f02498faad82917e19d5042'
CLIENT_SECRET = 'be9c7e5056fc460cb1d2af8d121efce3'
auth_url = 'https://accounts.spotify.com/api/token'

data2 = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}



auth_response = requests.post(auth_url, data2)

print(auth_response.status_code)
