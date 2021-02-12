# Most of the time, you can use the Seaborn API to modify your
# visualizations but sometimes it is helpful to use matplotlib's functions to customize your plots.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

fig, ax = plt.subplots()
sns.distplot(rents["fmr_3"], ax=ax)
ax.set(xlabel="3 Bedroom Fair Market Rent")
# ax.set_xlabel("3 Bedroom Fair Market Rent")
plt.show()
