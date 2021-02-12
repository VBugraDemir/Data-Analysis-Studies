# rectangular data -> tubular data -> it is represented as dataframe

# to quickly explore a data frame data.head() can be used
# data.info() column names data type and number of missing values
# data.shape returns a tuple that contains number of rows and columns (it's an attribute written without parenthesis)
# data.describe() summary statistics  (count (non-missing values),mean, median, min-max etc.)
# data.values (attribute) array of values
# data.columns data.index names (labels) of rows and columns
import pickle
import pandas as pd
newfile = open("homeless_data.pkl","rb")
homelessness = pickle.load(newfile)
print(homelessness.head())
print()
print(homelessness.info())
print()
print(homelessness.shape)
print()
print(homelessness.describe())
print()
print(homelessness.dtypes)
