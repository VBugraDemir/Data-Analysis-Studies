import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bike.csv")

# Create a jointplot of temp vs. casual riders
# Include a kdeplot over the scatter plot

g = sns.jointplot(x="temp", y="casual", kind="scatter", data=df, marginal_kws=dict(bins=10, rug=True)).plot_joint(sns.kdeplot)
plt.show()
# marginal için hist=False kde=True mesela
g = sns.jointplot(x="temp", y="registered", kind="scatter", data=df, marginal_kws=dict(bins=10, rug=True)).plot_joint(sns.kdeplot)
plt.show()
