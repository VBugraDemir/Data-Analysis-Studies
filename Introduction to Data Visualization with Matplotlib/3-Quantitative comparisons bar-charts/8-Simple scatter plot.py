import pandas as pd
import matplotlib.pyplot as plt

climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")

fig, ax = plt.subplots()
ax.scatter(climate_change["co2"], climate_change["relative_temp"])
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (C)")
plt.show()


fig, ax = plt.subplots()
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (C)")
plt.show()
