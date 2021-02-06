import pandas as pd
import matplotlib.pyplot as plt

ten_yr = pd.read_csv("ten_yr.csv",index_col=0)
dji = pd.read_csv("dji.csv", index_col=0)
print(ten_yr)

bond_perc = ten_yr.melt(id_vars="metric", var_name="date", value_name="close")
print(bond_perc)
bond_perc_close = bond_perc.query('metric == "close"')
print(dji)
dow_bond = pd.merge_ordered(dji, bond_perc_close, on="date", how="inner", suffixes=["_dow", "_bond"])

dow_bond.plot(y=["close_dow", "close_bond"], x="date", rot = 90)
plt.xlim(left = 0)
plt.xlim(right = 34)
plt.show()
