import pandas as pd

gdp = pd.read_csv("gdp_1980.csv", index_col=0)
gdp["date"] = pd.to_datetime(gdp["date"])

recession = pd.read_csv("recession.csv", index_col=0)
recession["date"] = pd.to_datetime(recession["date"])

gdp_recession = pd.merge_asof(gdp, recession, on = "date")
print(gdp_recession)

is_recession = ["r" if i =="recession" else "g" for i in gdp_recession["econ_status"]]

import matplotlib.pyplot as plt
gdp_recession.plot(kind="bar", x="date",y="gdp",color=is_recession, rot=90)
plt.show()