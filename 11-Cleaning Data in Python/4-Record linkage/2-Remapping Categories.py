import pandas as pd
from fuzzywuzzy import process

restaurants = pd.read_csv("restaurants_L2.csv", index_col=0, nrows=287)
restaurants = restaurants.drop("type", axis=1)
typos = pd.read_csv("typos.csv", index_col=0)
typos = typos.reset_index()
restaurants = restaurants.join(typos)

print(restaurants["cuisine_type"].unique())

matches = process.extract("italian", restaurants["cuisine_type"], limit = len(restaurants))
print(matches[0:5])

for match in matches:
    if match[1] >= 80:
        restaurants.loc[restaurants["cuisine_type"] == match[0], "cuisine_type"] = "italian"

print(restaurants)
# print(restaurants["cuisine_type"].unique())
categories = ["italian", "american", "asian"]
for cuisine in categories:
    matches = process.extract(cuisine, restaurants["cuisine_type"], limit= len(restaurants))
    for match in matches:
        if match[1] >= 80:
            restaurants.loc[restaurants['cuisine_type'] == match[0],"cuisine_type"] = cuisine
# print(restaurants["cuisine_type"].unique())
print(restaurants)
