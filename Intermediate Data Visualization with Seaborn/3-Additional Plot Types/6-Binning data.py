# When the data on the x axis is a continuous value, it can be useful to break it into
# different bins in order to get a better visualization of the changes in the data.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tuition = pd.read_csv("tui2.csv", index_col=0)
UG = pd.read_csv("UG.csv", index_col=0)
merged = tuition.join(UG)
# print(pd.merge(tuition, UG, left_index=True, right_index=True))

sns.regplot(data=merged, x="UG", y="Tuition", fit_reg=False)
plt.show()

sns.regplot(data=merged, x="UG", y="Tuition", x_bins=5)
plt.show()

sns.regplot(data=merged, x="UG", y="Tuition", x_bins=8)
plt.show()
