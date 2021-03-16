import pickle
import pandas as pd
newfile = open("homeless_data.pkl","rb")
homelessness = pickle.load(newfile)
# values columns and rows: DataFrames have three components: values, a column index, and a row index.
print(homelessness.values)
print()
print(homelessness.columns)
print()
print(homelessness.index)
print(homelessness.head())
