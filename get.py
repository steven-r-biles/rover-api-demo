import requests

API_URL = "http://localhost:8000"

response = requests.get(f"{API_URL}/mission/1/", headers={'Accept': 'application/json'})
print(response.json())

response = requests.get(f"{API_URL}/mission/1/", headers={'Accept': 'text/csv'})

filename = response.headers['Content-Disposition'].split('=')[1]

print(response.text)