import pickle
import pandas as pd
import matplotlib.pyplot as plt
newfile = open("avoplotto.pkl","rb")
avocados = pickle.load(newfile)
print(avocados.isna().any())
print()
print(avocados.isna().sum())

avocados.isna().sum().plot(kind = "bar")
plt.show()