import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/~guido/"
r = requests.get(url)
html_doc = r.text
print(html_doc)
print("---------------------------------------------------------------------------------")
soup = BeautifulSoup(html_doc,features="html.parser")
print(soup.prettify())