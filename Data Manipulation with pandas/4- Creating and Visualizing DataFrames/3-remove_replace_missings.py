import pickle
import pandas as pd
import matplotlib.pyplot as plt
newfile = open("avoplotto.pkl","rb")
avocados = pickle.load(newfile)

avocados_complete = avocados.dropna()
print(avocados_complete.isna().any())

# Since I dont have the data with nan values this code does not make any sense

# the column names that has the nan values are in the created list
# cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# histogram graph is created for each col. (3)
# avocados_2016[cols_with_missing].hist()
# plt.show()
#
# after that the missing values are replaced by 0
# avocados_filled = avocados_2016.fillna(0)
# avocados_filled[cols_with_missing].hist()
# plt.show()
