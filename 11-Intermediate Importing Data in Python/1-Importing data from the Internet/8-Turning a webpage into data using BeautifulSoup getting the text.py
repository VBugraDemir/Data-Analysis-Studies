# extracting information from HTML soup

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/~guido/"

r = requests.get(url)
html_doc = r.text

soup = BeautifulSoup(html_doc, features="html.parser")
# print(soup.prettify())
guido_title = soup.title
print(guido_title)
print("-------")
guido_text = soup.text  # or soup.get_text()
print(guido_text)
print("-------")
print(soup.get_text() == soup.text)

