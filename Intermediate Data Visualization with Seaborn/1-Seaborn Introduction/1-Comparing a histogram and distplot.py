# The pandas library supports simple plotting of data, which is very convenient when data is
# already likely to be in a pandas DataFrame.

# Seaborn generally does more statistical analysis on data and can provide more sophisticated
# insight into the data. compare a pandas histogram vs the seaborn distplot.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


school_imp = pd.read_csv("school_improvement.csv")
school_imp = school_imp.drop(["Unnamed: 0"], axis=1)

school_imp["Award_Amount"].plot.hist()
plt.show()

sns.distplot(school_imp["Award_Amount"])  # FutureWarning
plt.show()
sns.displot(school_imp["Award_Amount"], kde=True)
plt.show()