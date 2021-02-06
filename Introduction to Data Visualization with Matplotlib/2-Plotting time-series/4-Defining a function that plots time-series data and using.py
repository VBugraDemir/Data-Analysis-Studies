import pandas as pd
import matplotlib.pyplot as plt
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")

# If you want to plot two time-series variables that were recorded at the same time,
# you can add both of them to the same subplot.
#
# If the variables have very different scales, you'll want to make sure
# that you plot them in different twin Axes objects. These objects can share one
# axis (for example, the time, or x-axis) while not sharing the other (the y-axis).

def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params("y", colors=color)

fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative Temperature (Celsius)")
plt.show()

