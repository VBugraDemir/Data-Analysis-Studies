# You might think of this method when you are woking with
# data sampled from a process and the dates or times may not exactly align.
# similar to left join
# merge_asof has direction="nearest" or "forward"
import pandas as pd

jpm = pd.read_csv("jpm.csv", index_col=0)
# jpm["date_time"] = jpm["date_time"].astype("datetime64")
jpm["date_time"] = pd.to_datetime(jpm["date_time"])

wells = pd.read_csv("wells.csv", index_col=0)
wells["date_time"] = pd.to_datetime(wells["date_time"])

bac = pd.read_csv("bac.csv", index_col=0)
bac["date_time"] = pd.to_datetime(bac["date_time"])
jpm_wells = pd.merge_asof(jpm, wells, on="date_time", suffixes=["", "_wells"], direction= "nearest")

jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on="date_time", suffixes=["_jpm", "_bac"], direction="nearest")
print(jpm_wells_bac)
price_diff = jpm_wells_bac.diff()
print(price_diff)
import matplotlib.pyplot as plt
price_diff.plot(y=["close_jpm", "close_wells", "close_bac"])
plt.show()
