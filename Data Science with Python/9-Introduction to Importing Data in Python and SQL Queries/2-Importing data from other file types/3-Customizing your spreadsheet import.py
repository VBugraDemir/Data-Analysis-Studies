# skipping rows selecting columns and changing their names.

import pandas as pd

xls = pd.ExcelFile("battledeath.xlsx")

df1 = xls.parse(0, skiprows=[1], names=["Country", "AAM due to War (2002)"])
print(df1.head())

df2 = xls.parse(1, skiprows=[1], usecols=[0], names=["Country"])
print(df2.head())
