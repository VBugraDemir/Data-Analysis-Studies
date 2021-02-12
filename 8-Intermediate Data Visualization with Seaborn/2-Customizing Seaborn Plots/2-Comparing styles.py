import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

sns.set_style("dark")
sns.distplot(rents["fmr_2"])
plt.show()

sns.set_style("whitegrid")
sns.distplot(rents["fmr_2"])
plt.show()