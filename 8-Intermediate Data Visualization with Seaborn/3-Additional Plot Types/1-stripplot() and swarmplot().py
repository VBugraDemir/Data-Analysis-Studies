import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

school_imp = pd.read_csv("school_improvement.csv")
school_imp = school_imp.drop("Unnamed: 0", axis=1)

sns.stripplot(x="Award_Amount", y="Model Selected", data=school_imp, jitter=True)
plt.show()

sns.swarmplot(x="Award_Amount", y="Model Selected", data=school_imp, hue="Region")
plt.show()
# does not scale well to large datasets
