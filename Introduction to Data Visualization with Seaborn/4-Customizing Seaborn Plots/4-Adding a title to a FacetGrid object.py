# catplot and relplot create FacetGrid objects that consist of one or more AxesSubplots
# scatterplot countplot etc. create AxesSubplot only single plot


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")
sns.set_style("darkgrid")
g = sns.relplot(x="weight", y="horsepower", data=mpg, kind="scatter")
g.fig.suptitle("Car Weight vs. Horsepower")
plt.show()
