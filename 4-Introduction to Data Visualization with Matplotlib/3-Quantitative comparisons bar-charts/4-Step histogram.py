import pandas as pd
import matplotlib.pyplot as plt

summer = pd.read_csv("summer2016.csv")
mens_rowing = summer[summer["Sport"] == "Rowing"]
mens_gymnastics = summer[summer["Sport"] == "Gymnastics"]

fig, ax = plt.subplots()
ax.hist(mens_rowing["Weight"], label="Rowing", histtype="step", bins=5)
ax.hist(mens_gymnastics["Weight"], label="Gymnastics", histtype="step", bins=5)
ax.legend()
plt.show()
