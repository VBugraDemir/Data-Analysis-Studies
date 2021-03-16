import pickle
import pandas as pd

newfile = open("taglines.p","rb")
taglines = pickle.load(newfile)

#  If your goal is to enhance or enrich a dataset, then you do not want to lose any of your original data.
#  A left join will do that by returning all of the rows of your left table, while using an inner join may
#  result in lost data if it does not exist in both tables.

toy_story_list = {
    "id":[10193, 863, 862],
    "title":["Toy Story 3", "Toy Story 2", "Toy Story"],
    "popularity":[59.995418, 73.575118, 73.640445],
    "release_date":["2010-06-16", "1999-10-30", "1995-10-30"]
}

toy_story = pd.DataFrame(toy_story_list)
toy_story["release_date"] = pd.to_datetime(toy_story["release_date"])

toystory_tag = toy_story.merge(taglines, on = "id", how = "left")
print(toystory_tag)
print()
toystory_tag = toy_story.merge(taglines, on = "id")
print(toystory_tag)
