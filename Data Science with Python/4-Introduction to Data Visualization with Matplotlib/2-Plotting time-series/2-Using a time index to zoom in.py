import pandas as pd
import matplotlib.pyplot as plt
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")

seventies = climate_change["1970-01-01":"1979-12-31"]

fig, ax = plt.subplots()
ax.plot(seventies.index, seventies["co2"])

plt.show()
