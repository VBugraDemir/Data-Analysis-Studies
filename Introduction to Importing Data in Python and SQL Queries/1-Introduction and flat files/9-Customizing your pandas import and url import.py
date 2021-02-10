import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlretrieve

data = pd.read_csv("corrupted.txt", sep="\t", comment="#", na_values="Nothing")
print(data)
# na_values takes a list of strings to recognize as NA/NaN, in this case the string 'Nothing'.
pd.set_option("display.max_columns", None)
print(data.head(7))
pd.DataFrame.hist(data[["Age"]]) # data["Age"].hist()
plt.xlabel("Age (years)")
plt.ylabel("count")
plt.show()

# retrieving files from urls and saving them locally
url = "https://raw.githubusercontent.com/wblakecannon/DataCamp/master/05-importing-data-in-python-(part-1)/_datasets/titanic_corrupt.txt"

urlretrieve(url, "cor.csv")

