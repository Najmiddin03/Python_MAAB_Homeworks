import requests

api_key = "975469a6"

url = f"https://www.omdbapi.com/?i=tt3896198&apikey={api_key}"

response = requests.get(url)

print(response.json())
