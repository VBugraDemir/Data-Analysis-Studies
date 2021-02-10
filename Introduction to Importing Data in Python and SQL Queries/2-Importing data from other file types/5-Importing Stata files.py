import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_stata("disarea.dta")
print(df.head())

pd.DataFrame.hist(df[["disa10"]])
plt.xlabel("Extent of disease")
plt.ylabel("Number of countries")
plt.show()
