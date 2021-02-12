# relational plots = scatter and line plots
# in scatter plot each plot is an independent observation
# line plot are the visualization of choice to track the same thing over time.

import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

sns.relplot(x="model_year", y="mpg", kind="line",data=mpg)
plt.show()
# how the average miles per gallon achieved by cars has changed over time, shaded areas are
# confidence interval for the mean.

sns.lineplot(x="model_year", y="mpg", data=mpg)
plt.show()


