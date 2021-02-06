import pandas as pd
import matplotlib.pyplot as plt
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")

fig, ax = plt.subplots()

ax.plot(climate_change.index, climate_change["relative_temp"])
ax.annotate(">1 degree", xy=(pd.Timestamp("2015-10-26"), 1)) # square brackets are also accpeted xy
plt.show()


def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params("y", colors=color)


fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temp (Celsius)")
ax2.annotate(">1 degree", xy=[pd.Timestamp("2015-11-06"), 1.04], xytext=(pd.Timestamp("2008-10-06"), -0.2),
             arrowprops={"arrowstyle":"->", "color":"gray"})
plt.show()
