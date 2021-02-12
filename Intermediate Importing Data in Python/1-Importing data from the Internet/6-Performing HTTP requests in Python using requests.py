# Now that you've got your head and hands around making HTTP requests using the urllib package, you're
# going to figure out how to do the same using the higher-level requests library.

import requests

url = "http://www.datacamp.com/teach/documentation"

r = requests.get(url)
html = r.text
print(html)

url2 = "https://campus.datacamp.com/courses/1606/4135?ex=2"
r2 = requests.get(url2)
html2 = r2.text
print(html2)
# it is better than before. (5-Printing HTTP... all codes in a single line.)
