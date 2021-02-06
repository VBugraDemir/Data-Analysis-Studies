import pandas as pd

inflation = pd.read_csv("inflation2.csv", index_col = 0)
print(inflation)
melted_inf = inflation.melt(id_vars=["country", "indicator"], value_name= "annual", var_name="year")
print(melted_inf)
# This is often a much more computer friendly format.
