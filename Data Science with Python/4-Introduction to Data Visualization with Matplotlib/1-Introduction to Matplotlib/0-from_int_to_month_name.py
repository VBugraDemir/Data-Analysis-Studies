import pandas as pd
import matplotlib.pyplot as plt


seattle_weather = pd.read_csv("seattle_weather.csv")
austin_weather = pd.read_csv("austin_weather.csv")
seattle_weather["MONTH"] = pd.to_datetime(seattle_weather["DATE"], format = "%m").dt.month_name().str.slice(stop=3)
print(seattle_weather[["DATE","MONTH"]])
