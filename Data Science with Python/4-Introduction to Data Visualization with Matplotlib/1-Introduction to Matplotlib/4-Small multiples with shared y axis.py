import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv("seattle_weather2.csv")
austin_weather = pd.read_csv("austin_weather.csv")

fig, ax = plt.subplots(2, 1, sharey=True)
# the ax array is one dimensional so needs one index to acces the element of this array

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color="b")
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color="b", linestyle="--")
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color="b", linestyle="--")

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r")
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color="r", linestyle="--")
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color="r", linestyle="--")
plt.show()
