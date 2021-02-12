import pickle
import pandas as pd

newfile = open("licenses.p","rb")
licenses = pickle.load(newfile)

newfile2 = open("land_use.p","rb")
land_use = pickle.load(newfile2)

newfile3 = open("census.p","rb")
census = pickle.load(newfile3)
pd.set_option("display.max_columns", None)
land_cen_lic = land_use.merge(census, on = "ward").merge(licenses, on = "ward", suffixes = ["_cen", "_lic"])
pop_vac_lic = land_cen_lic.groupby(["ward", "pop_2010", "vacant"], as_index = False).agg({"account":"count"})
# as_index = False so the grouppedby columns are not set as index so we can use the old index
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant", "account", "pop_2010"], ascending= [False, True, True])
print(sorted_pop_vac_lic.head())
