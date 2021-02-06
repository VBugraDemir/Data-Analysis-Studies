import pandas as pd
import matplotlib.pyplot as plt


seattle_weather = pd.read_csv("seattle_weather2.csv")
austin_weather = pd.read_csv("austin_weather.csv")


fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"], color="b", marker="o", linestyle="--")
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r", marker="v", linestyle="--")
plt.show()
