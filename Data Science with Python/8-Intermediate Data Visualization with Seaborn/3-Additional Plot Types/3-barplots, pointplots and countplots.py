# The final group of categorical plots are barplots, pointplots and
# countplot which create statistical summaries of the data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

school_imp = pd.read_csv("school_improvement.csv")
school_imp = school_imp.drop("Unnamed: 0", axis=1)

sns.countplot(data=school_imp, y="Model Selected", hue="Region")
plt.show()

sns.pointplot(data=school_imp, x="Model Selected", y="Award_Amount", capsize=0.1)
plt.show()

sns.barplot(data=school_imp, x="Model Selected", y="Award_Amount", hue="Region")
plt.show()
