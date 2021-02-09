import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bike.csv")

# sns.set_style("whitegrid")
# g = sns.JointGrid(x="hum",
#             y="total_rentals",
#             data=df,
#             xlim=(0.1, 1.0))
#
# g.plot(sns.regplot, sns.distplot)
#
# plt.show()

sns.jointplot(x="hum", y="total_rentals", kind="reg", data=df)
plt.show()
