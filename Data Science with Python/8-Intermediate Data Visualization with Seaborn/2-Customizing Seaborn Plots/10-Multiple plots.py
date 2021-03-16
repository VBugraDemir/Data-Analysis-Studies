import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

sns.set_style("darkgrid")

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)
sns.distplot(rents["fmr_1"], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500))
sns.distplot(rents["fmr_2"], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100, 1500))
plt.show()
#
# fig, ax = plt.subplots(1,2, sharey=True)
# sns.distplot(rents["fmr_1"], ax=ax[0])
# ax[0].set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500))
# sns.distplot(rents["fmr_2"], ax=ax[1])
# ax[1].set(xlabel="2 Bedroom Fair Market Rent", xlim=(100, 1500))
# plt.show()
