import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avo = pickle.load(newfile)

print(avo.iloc[[22], [1]])
print(avo.iloc[0:5])
print(avo.iloc[:, 2:4])
print(avo.iloc[0:5,2:4])
