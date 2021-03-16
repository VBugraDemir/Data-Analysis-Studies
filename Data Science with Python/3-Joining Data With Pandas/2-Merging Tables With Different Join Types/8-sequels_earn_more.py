import pickle
import pandas as pd
import matplotlib.pyplot as plt

newfile = open("sequels.p","rb")
sequels = pickle.load(newfile)
sequels = sequels.set_index("id")

newfile1 = open("financials.p","rb")
financials = pickle.load(newfile1)
financials = financials.set_index("id")

# sequels["sequel"] = sequels["sequel"].astype(float)
# sequels = sequels.replace("<NA>","NaN")
sequels["sequel"]=sequels["sequel"].apply(pd.to_numeric, errors='coerce',downcast='integer')
pd.options.display.float_format = '{:.0f}'.format
# a column that consists of NaN values is always float64 (not int)

sequels_fin = sequels.merge(financials, on='id', how='left')
pd.set_option("display.max_columns", None)

orig_seq = sequels_fin.merge(sequels_fin, left_on = "sequel", right_on = "id", right_index = True, suffixes = ["_org", "_seq"])
orig_seq["diff"] = orig_seq["revenue_seq"] - orig_seq["revenue_org"]
titles_dif = orig_seq[["title_org", "title_seq", "diff"]]
print(titles_dif.sort_values("diff", ascending = False))
