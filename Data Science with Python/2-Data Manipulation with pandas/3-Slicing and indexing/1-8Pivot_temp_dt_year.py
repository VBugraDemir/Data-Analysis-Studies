import pandas as pd
temperature = pd.read_csv("temperature.csv",index_col=0)
temperature["date"] = pd.to_datetime(temperature["date"])

temperature["year"] = temperature["date"].dt.year
print(temperature)