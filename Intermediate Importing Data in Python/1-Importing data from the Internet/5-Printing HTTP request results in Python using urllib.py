from urllib.request import Request, urlopen

url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

request = Request(url)
response = urlopen(request)

html = response.read()
print(html)

response.close()
