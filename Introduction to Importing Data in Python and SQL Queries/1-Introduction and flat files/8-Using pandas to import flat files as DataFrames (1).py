import pandas as pd
df = pd.read_csv("titanic.csv")
print(df.head())

data = pd.read_csv("MNIST.txt", header=None, nrows=5)
# nrows to limit the number of rows that to be read
print(data)
data_array = data.values
print(type(data_array))

