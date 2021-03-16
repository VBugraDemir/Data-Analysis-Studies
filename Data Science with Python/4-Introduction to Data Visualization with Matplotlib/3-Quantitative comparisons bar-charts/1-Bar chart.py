import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv("medals_by_country_2016.csv", index_col=0)

medals["Gold"].plot(kind="bar",rot=90)
plt.ylabel("Number of Medals")
plt.legend()
plt.show()

# As seen above by plotting any data frame directly without defining any ax or fig labels are created
# and ticks are rotated automatically
fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"], label = "Gold")
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of Medals")
plt.legend()
plt.show()


