import pandas as pd
import matplotlib.pyplot as plt
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")

fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["relative_temp"])
ax.set_xlabel("Time")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()

