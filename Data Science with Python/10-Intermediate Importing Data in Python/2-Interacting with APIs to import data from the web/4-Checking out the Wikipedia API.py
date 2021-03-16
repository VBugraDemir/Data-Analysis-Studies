import requests
import json
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

r = requests.get(url)

json_data = r.json()
print(json_data["query"]["pages"]["24768"]["extract"])
