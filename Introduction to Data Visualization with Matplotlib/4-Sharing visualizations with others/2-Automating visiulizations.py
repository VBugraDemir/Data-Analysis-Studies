import pandas as pd
import matplotlib.pyplot as plt

summer = pd.read_csv("summer2016.csv", index_col=0)

sports = summer["Sport"].unique()[:10]

fig, ax = plt.subplots()
for sport in sports:
    sport_df = summer[summer["Sport"] == sport]
    ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())
    print(sport_df["Weight"].std())
ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)
plt.show()
fig.savefig("Weights_2016.png")

