import json
import requests

url = "http://www.omdbapi.com/?apikey=72bc447a&t=social+network"

r = requests.get(url)

json_data = r.json()

for k in json_data.keys():
    print(k, ": ", json_data[k])
