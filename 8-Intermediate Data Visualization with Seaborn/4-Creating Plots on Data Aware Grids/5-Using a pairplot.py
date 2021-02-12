import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv("insurance.csv")

sns.pairplot(data=insurance, vars=["fatal_collisions", "premiums"], kind="scatter", diag_kws={"bins":10})
plt.show()

sns.pairplot(data=insurance, vars=["fatal_collisions", "premiums"], kind="scatter", diag_kind="hist", hue="Region",
             palette="RdBu", diag_kws={"alpha":.5,"bins":10})
plt.show()
