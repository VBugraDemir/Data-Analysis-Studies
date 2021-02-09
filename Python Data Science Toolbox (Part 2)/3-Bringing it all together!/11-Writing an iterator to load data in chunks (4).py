import pandas as pd
import matplotlib.pyplot as plt

urb_pop_reader = pd.read_csv("world_dev_ind.csv", chunksize=1000)

data= pd.DataFrame()

for df_urb_pop in urb_pop_reader:
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB'].copy()
    # pops = zip(df_pop_ceb["Total Population"], df_pop_ceb["Urban population (% of total)"])
    # pops_list = list(pops)
    # df_pop_ceb["Total Urban Population"] = [int(i[0] * i[1] * 0.01) for i in pops_list]
    df_pop_ceb["Total Urban Population"] = df_pop_ceb["Total Population"] * df_pop_ceb["Urban population (% of total)"] / 100
    data = data.append(df_pop_ceb)


data.plot(kind="scatter", x="Year", y="Total Urban Population")
plt.show()

urb_pop_reader = pd.read_csv("world_dev_ind.csv", chunksize=1000)

data= pd.DataFrame()

for df_urb_pop in urb_pop_reader:
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB'].copy()
    pops = zip(df_pop_ceb["Total Population"], df_pop_ceb["Urban population (% of total)"])
    pops_list = list(pops)
    df_pop_ceb["Total Urban Population"] = [int(i[0] * i[1] * 0.01) for i in pops_list]
    # df_pop_ceb["Total Urban Population"] = df_pop_ceb["Total Population"] * df_pop_ceb["Urban population (% of total)"] / 100
    data = data.append(df_pop_ceb)


data.plot(kind="scatter", x="Year", y="Total Urban Population")
plt.show()
