import pickle
import pandas as pd

newfile = open("movies.p","rb")
movies = pickle.load(newfile)

newfile2 = open("movie_to_genres.p","rb")
genres = pickle.load(newfile2)

action_movies = genres[genres["genre"] == "Action"]

scifi_movies = genres[genres["genre"] == "Science Fiction"]

action_scifi = action_movies.merge(scifi_movies, on = "movie_id", how = "right", suffixes = ["_act", "_sci"])
scifi_only = action_scifi[action_scifi["genre_act"].isnull()]
movies_and_scifi_only = movies.merge(scifi_only, left_on = "id", right_on = "movie_id")
pd.set_option("display.max_columns", None)
print(movies_and_scifi_only)
