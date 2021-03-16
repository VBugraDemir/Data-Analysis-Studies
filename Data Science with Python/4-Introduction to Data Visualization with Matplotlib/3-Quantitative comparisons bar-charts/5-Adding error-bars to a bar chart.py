# histograms are to make comparisions
# to make comparisons more formal we can use error bars in plots

import pandas as pd
import matplotlib.pyplot as plt

summer = pd.read_csv("summer2016.csv")
mens_rowing = summer[summer["Sport"] == "Rowing"]
mens_gymnastics = summer[summer["Sport"] == "Gymnastics"]

fig, ax = plt.subplots()
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr= mens_gymnastics["Height"].std())
ax.set_ylabel("Height (cm)")
plt.show()

