import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

rents["fmr_2"].plot.hist()
plt.show()

rents["fmr_2"].hist()
plt.show()

sns.set()
rents["fmr_2"].plot.hist()
plt.show()
