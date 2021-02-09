import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv("insurance.csv")

sns.lmplot(x="insurance_losses", y="premiums", data=insurance, row="Region")
plt.show()

sns.regplot(x="insurance_losses", y="premiums", data=insurance, row="Region")
plt.show()

# since regplot does not support row argument it throws an error.
