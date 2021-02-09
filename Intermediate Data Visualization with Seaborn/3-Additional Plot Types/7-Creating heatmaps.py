import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

daily_show = pd.read_csv("daily_show.csv")

pd_crosstab = pd.crosstab(daily_show["Group"], daily_show["YEAR"])
print(pd_crosstab)

sns.heatmap(pd_crosstab)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()
