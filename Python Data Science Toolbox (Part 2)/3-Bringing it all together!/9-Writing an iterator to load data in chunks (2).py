import pandas as pd

urb_pop_reader = pd.read_csv("world_dev_ind.csv", chunksize=1000)
df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())

df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == "CEB"]
pops = zip(df_pop_ceb["Total Population"], df_pop_ceb["Urban population (% of total)"])
pops_list = list(pops)

print(pops_list)
