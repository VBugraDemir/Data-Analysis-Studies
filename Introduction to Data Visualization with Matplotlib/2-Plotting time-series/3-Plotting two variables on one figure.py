import pandas as pd
import matplotlib.pyplot as plt

# scales would be different for different data so we use axtwinx

climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")

fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["co2"],"b")
ax2 = ax.twinx()
ax2.plot(climate_change.index, climate_change["relative_temp"],"r")
plt.show()
