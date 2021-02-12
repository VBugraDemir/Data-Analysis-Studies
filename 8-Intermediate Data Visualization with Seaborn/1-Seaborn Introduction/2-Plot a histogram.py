#  The KDE helps to smooth the distribution and is a useful way to look at the data.
#  However, Seaborn can also support the more standard histogram approach if that is
#  more meaningful for your analysis.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

school_imp = pd.read_csv("school_improvement.csv")
school_imp = school_imp.drop("Unnamed: 0", axis=1)

sns.displot(school_imp["Award_Amount"], kde=False, bins=20)
plt.show()
