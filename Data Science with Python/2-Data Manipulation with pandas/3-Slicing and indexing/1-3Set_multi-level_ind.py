import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)

avo_ind = avo.set_index(["size","type"])
# print(avo_ind.loc[("small","organic")])
rows_to_keep = [("small","organic"),("extra_large","conventional")]
print(avo_ind.loc[rows_to_keep])