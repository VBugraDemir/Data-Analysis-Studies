import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv("seattle_weather2.csv")
austin_weather = pd.read_csv("austin_weather.csv")

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"])
ax[0, 1].plot(seattle_weather["MONTH"],seattle_weather["MLY-TAVG-NORMAL"])

ax[1, 0].plot(austin_weather["MONTH"],austin_weather["MLY-PRCP-NORMAL"])
ax[1, 1].plot(austin_weather["MONTH"],austin_weather["MLY-TAVG-NORMAL"])
plt.show()

