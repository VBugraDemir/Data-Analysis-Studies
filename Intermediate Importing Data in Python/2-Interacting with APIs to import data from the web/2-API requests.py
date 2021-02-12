import requests

url = "http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network"
r = requests.get(url)

print(r.text)
