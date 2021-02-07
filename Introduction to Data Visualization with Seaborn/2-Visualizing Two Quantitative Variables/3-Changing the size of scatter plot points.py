import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

sns.relplot(x="horsepower", y="mpg", data=mpg, kind="scatter",
            size="cylinders", hue="cylinders")
plt.show()
