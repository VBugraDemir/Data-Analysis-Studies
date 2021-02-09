import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

sns.set_style("white")
sns.lmplot(data=rents, x="pop2010", y="fmr_2")
sns.despine(left=True, bottom=True)


sns.set_style("white")
sns.lmplot(data=rents, x="pop2010", y="fmr_2")
sns.despine()
plt.show()
