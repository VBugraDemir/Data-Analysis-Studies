import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line",  ci=None,
            style="origin", hue="origin", markers=True, dashes=False)
plt.show()
