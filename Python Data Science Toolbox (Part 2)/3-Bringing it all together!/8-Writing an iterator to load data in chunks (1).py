import pandas as pd

df_reader = pd.read_csv("world_dev_ind.csv", chunksize=10)

print(next(df_reader))
print(next(df_reader))
