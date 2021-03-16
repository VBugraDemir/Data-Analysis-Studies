import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bike.csv")

sns.jointplot(x="hum", y="total_rentals", kind="reg", data=df, order=2, xlim=(0,1))
plt.show()

sns.jointplot(x="hum", y="total_rentals", kind="resid", data=df, order=2, marginal_kws={"kde":True})
# marginal için hist=False kde=True mesela
plt.show()
