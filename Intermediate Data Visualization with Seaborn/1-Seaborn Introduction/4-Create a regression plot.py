# Regression analysis is bivariate because relationship between two variables are considered
# regplot is lower level and lmplot is higher level


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv("insurance.csv")

sns.regplot(x="insurance_losses", y="premiums", data=insurance)


sns.lmplot(x="insurance_losses", y="premiums", data=insurance)
plt.show()
