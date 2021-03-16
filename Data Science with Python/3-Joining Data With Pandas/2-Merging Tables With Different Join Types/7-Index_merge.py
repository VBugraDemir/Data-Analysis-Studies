import pickle
import pandas as pd
import matplotlib.pyplot as plt

newfile = open("movies.p","rb")
movies = pickle.load(newfile)
movies = movies.set_index("id")

newfile1 = open("ratings.p","rb")
ratings = pickle.load(newfile1)
ratings = ratings.set_index("id")

movies_ratings = movies.merge(ratings, on = "id", how = "left")
print(movies_ratings)
