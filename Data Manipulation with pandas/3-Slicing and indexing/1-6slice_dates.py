import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)
print(avo)

# slicing by booleans
avo_bool = avo[(avo["date"] >= "2015-01-01") & (avo["date"] <= "2017-12-31")]
print(avo_bool)

# slicing by .loc
avo_ind = avo.set_index("date").sort_index()
print(avo_ind.loc["2017":"2018"])
print(avo_ind.loc["2017-07":"2018-05"])
