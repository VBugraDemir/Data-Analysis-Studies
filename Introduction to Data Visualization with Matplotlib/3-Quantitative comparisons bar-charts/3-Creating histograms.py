import pandas as pd
import matplotlib.pyplot as plt

summer = pd.read_csv("summer2016.csv")
mens_rowing = summer[summer["Sport"] == "Rowing"]
mens_gymnastics = summer[summer["Sport"] == "Gymnastics"]

fig, ax = plt.subplots()
ax.hist(mens_rowing["Weight"])
ax.hist(mens_gymnastics["Weight"])
ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")
plt.show()
