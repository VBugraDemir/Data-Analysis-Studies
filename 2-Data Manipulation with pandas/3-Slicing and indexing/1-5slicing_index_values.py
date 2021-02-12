import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)

avo_ind = avo.set_index(["size","type"])
# we have to sort it first
avo_ind_srt = avo_ind.sort_index()
print(avo_ind_srt.loc["extra_large":"small"])
print(avo_ind_srt.loc[("extra_large","organic"):("small","conventional")])
# previous ones can also be done without loc but to choose from both rows and columns loc is a must
print(avo_ind_srt.loc[("extra_large","organic"):("small","conventional"), "year":"nb_sold"])
