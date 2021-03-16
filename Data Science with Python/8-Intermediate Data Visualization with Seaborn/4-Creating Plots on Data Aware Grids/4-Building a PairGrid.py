import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv("insurance.csv")

g = sns.PairGrid(insurance, vars=["fatal_collisions", "premiums"])
g2 = g.map(plt.scatter)
plt.show()

g = sns.PairGrid(insurance, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist)
g3 = g.map_offdiag(plt.scatter)

sns.pairplot(insurance[["fatal_collisions", "premiums"]])
plt.show()