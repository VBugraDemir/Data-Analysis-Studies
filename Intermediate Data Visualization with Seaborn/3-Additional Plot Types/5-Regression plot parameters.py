import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tuition = pd.read_csv("tui2.csv", index_col=0)

sns.regplot(data=tuition, x="PCTPELL", y="Tuition")
plt.show()

sns.regplot(data=tuition, x="PCTPELL", y="Tuition", x_bins=5)
plt.show()

sns.regplot(data=tuition, x="PCTPELL", y="Tuition", x_bins=5, order=2)
plt.show()
