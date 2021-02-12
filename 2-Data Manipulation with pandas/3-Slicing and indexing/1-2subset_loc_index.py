import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)

# subsetting by isin and loc after setting index
sizes = ["large","extra_large"]
print(avo[avo["size"].isin(sizes)])
avo_ind = avo.set_index("size")
print(avo_ind.loc[sizes])