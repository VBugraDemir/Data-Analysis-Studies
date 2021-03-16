import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)
# pandas allows you to designate columns as an index.
print(avo.head())
avo_ind = avo.set_index("size")
print(avo_ind)
print(avo_ind.reset_index())
print(avo_ind.reset_index("size",drop=True))