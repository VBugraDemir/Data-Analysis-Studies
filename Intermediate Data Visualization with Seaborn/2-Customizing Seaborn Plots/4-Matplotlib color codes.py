# A quick way to change colors is to use the standard matplotlib color codes.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

sns.set(color_codes=True)
sns.distplot(rents["fmr_3"], color="m")
plt.show()
