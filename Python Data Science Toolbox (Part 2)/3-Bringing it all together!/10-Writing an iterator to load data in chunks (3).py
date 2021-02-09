import pandas as pd
import matplotlib.pyplot as plt

urb_pop_reader = pd.read_csv("world_dev_ind.csv", chunksize=1000)
df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())

df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == "CEB"].copy()  # with .copy() we can avoid SettingWithCopyWarning.
# pops = zip(df_pop_ceb["Total Population"], df_pop_ceb["Urban population (% of total)"])
# pops_list = list(pops)
print(df_pop_ceb.head())
df_pop_ceb['Total Urban Population'] = (df_pop_ceb['Total Population'] * df_pop_ceb['Urban population (% of total)'])
print((df_pop_ceb['Total Urban Population']))
df_pop_ceb.plot(kind="scatter", x="Year", y="Total Urban Population")
plt.show()
