import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

school_imp = pd.read_csv("school_improvement.csv")

sns.distplot(school_imp["Award_Amount"], hist=False, rug=True, kde_kws={"shade":True})
plt.show()

# This plot can be really useful for understanding how the award dollars were distributed.
