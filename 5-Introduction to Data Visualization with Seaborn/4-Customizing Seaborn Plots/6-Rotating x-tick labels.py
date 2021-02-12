import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")

sns.catplot(x="origin", y="acceleration", data=mpg, kind="point", join=False, capsize=0.2)
plt.xticks(rotation=90)
plt.show()
