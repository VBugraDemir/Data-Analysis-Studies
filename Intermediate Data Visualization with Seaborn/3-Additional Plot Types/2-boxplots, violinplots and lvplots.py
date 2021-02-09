import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

school_imp = pd.read_csv("school_improvement.csv")
school_imp = school_imp.drop("Unnamed: 0", axis=1)

sns.boxplot(x="Award_Amount", y="Model Selected", data=school_imp)
plt.show()

sns.violinplot(x="Award_Amount", y="Model Selected", data=school_imp, palette="husl")
plt.show()

sns.boxenplot(x="Award_Amount", y="Model Selected", data=school_imp, palette="Paired", hue="Region")
plt.show()

# the lvplot is removed and
