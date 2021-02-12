import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)

avo_ind = avo.set_index(["year","avg_price"])
print(avo_ind)
print(avo_ind.sort_index(level = "avg_price",ascending = True))
# levels can be 0,1 etc...
print(avo_ind.sort_index(level=["year","avg_price"],ascending=[True, False]))
