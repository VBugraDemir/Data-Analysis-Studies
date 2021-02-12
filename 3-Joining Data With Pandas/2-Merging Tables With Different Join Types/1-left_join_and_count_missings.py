import pickle
import pandas as pd

newfile = open("movies.p","rb")
movies = pickle.load(newfile)

newfile2 = open("financials.p","rb")
financials = pickle.load(newfile2)

movies_financials = movies.merge(financials, on = "id", how = "left") # default value of how is "inner"
print(movies_financials["budget"].isna().sum())