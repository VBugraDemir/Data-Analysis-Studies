import pandas as pd
import matplotlib.pyplot as plt

summer = pd.read_csv("summer2016.csv")
mens_rowing = summer[summer["Sport"] == "Rowing"]
mens_gymnastics = summer[summer["Sport"] == "Gymnastics"]

fig, ax = plt.subplots()
ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")
plt.show()
