import pandas as pd
import matplotlib.pyplot as plt

ur_wide = pd.read_csv("ur_wide.csv", index_col=0)
ur_wide["year"] = ur_wide["year"].astype("str")
print(ur_wide)
ur_tall = ur_wide.melt(id_vars="year", var_name="month", value_name="unempl_rate")
ur_tall["date"] = pd.to_datetime(ur_tall["year"] + "-" + ur_tall["month"])
ur_sorted = ur_tall.sort_values("date")
print(ur_sorted)

ur_sorted.plot(x="date",y="unempl_rate")
plt.show()
