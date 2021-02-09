import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rents = pd.read_csv("market_rent.csv")

for p in ["bright", "colorblind"]:
    sns.set_palette(p)
    sns.distplot(rents["fmr_3"])
    plt.show()

