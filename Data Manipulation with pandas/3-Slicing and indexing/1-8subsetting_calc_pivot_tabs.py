import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)
avo["date"] = pd.to_datetime(avo["date"])
price_by_type_size_vs_year = avo.pivot_table(values = "avg_price", index =["size","type"],columns = "year")
print(price_by_type_size_vs_year)
print()
print(price_by_type_size_vs_year.loc["extra_large":"large"])
print()
print(price_by_type_size_vs_year.loc[("extra_large","organic"):("large","organic")])
print()
print(price_by_type_size_vs_year.loc[("extra_large","organic"):("large","organic"),2017:2018])
print()
mean_by_year = price_by_type_size_vs_year.mean(axis = "index")
print(mean_by_year)
print()
print(mean_by_year[mean_by_year == mean_by_year.max()]) #****
print()
mean_by_type = price_by_type_size_vs_year.mean(axis = "columns")
print(mean_by_type)
print()
print(mean_by_type[mean_by_type == mean_by_type.min()])

