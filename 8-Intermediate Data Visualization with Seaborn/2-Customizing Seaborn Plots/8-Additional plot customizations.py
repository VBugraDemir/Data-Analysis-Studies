import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

sns.set_style("darkgrid")
fig, ax = plt.subplots()
sns.distplot(rents["fmr_1"], ax=ax)
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100, 1500),
       title="US Rent")
plt.show()
