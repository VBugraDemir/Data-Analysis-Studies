import pandas as pd
import matplotlib.pyplot as plt
import datetime
gdp = pd.read_csv("gdp_china_us.csv", index_col= 0)
pop = pd.read_csv("pop.csv", index_col= 0)

gdp_pop = pd.merge_ordered(gdp, pop, on = ["country", "date"], fill_method="ffill")
gdp_pop["gdp_per_capita"] = gdp_pop["gdp"] / gdp_pop["pop"]

gdp_pivot = gdp_pop.pivot(values="gdp_per_capita", index="date", columns="country")
print(gdp_pop)
print(gdp_pivot)
recent_gdp_pop = gdp_pivot.query('date >= "2016-01-01"')
print(recent_gdp_pop)
recent_gdp_pop.plot(rot = 90)
# plt.xlim(left = 0)
# plt.xlim(right = 11)
plt.show()
