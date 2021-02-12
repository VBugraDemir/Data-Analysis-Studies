import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

# to visualize how the distribution of miles per gallon has changed over time.

sns.relplot(x="model_year", y="mpg", data=mpg, kind="line", ci="sd")
plt.show()
