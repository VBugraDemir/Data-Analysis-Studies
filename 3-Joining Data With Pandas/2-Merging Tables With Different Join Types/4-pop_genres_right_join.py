import pickle
import pandas as pd
import matplotlib.pyplot as plt

newfile = open("movies.p","rb")
movies = pickle.load(newfile)

newfile2 = open("movie_to_genres.p","rb")
genres = pickle.load(newfile2)

pop_movies = movies.sort_values("popularity", ascending = False).iloc[0:10]
genres_movies = genres.merge(pop_movies, how = "right", left_on = "movie_id", right_on = "id")

genre_count = genres_movies.groupby("genre").agg({"id":"count"})
genre_count.plot(kind = "bar")
plt.show()

# genre_count = genres_movies.groupby("genre")["id"].count()
# genre_count.plot(kind = "bar")
# plt.show()


