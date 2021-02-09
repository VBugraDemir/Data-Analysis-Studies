import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

mean = 706.3254351016984
median = 634.0

sns.set_palette("bright")
sns.set_style("darkgrid")
fig, ax = plt.subplots()

# axvline (x=...) and axhline (y=...)

sns.distplot(rents["fmr_1"], ax=ax)
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500), title="US Rent")
ax.axvline(x=median, color="m", label="Median", linestyle="--", linewidth=2)
ax.axvline(x=mean, color="b", label="Mean", linestyle="--", linewidth=2)
ax.legend()
plt.show()
