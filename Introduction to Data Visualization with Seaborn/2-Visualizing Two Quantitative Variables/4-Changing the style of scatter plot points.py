import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

sns.relplot(x="acceleration", y="mpg", data=mpg, kind="scatter", hue="origin", style="origin")
plt.show()
