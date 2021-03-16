import pandas as pd

xls = pd.ExcelFile("battledeath.xlsx")
print(xls.sheet_names)

df1 = xls.parse("2004")
print(df1)

df2 = xls.parse(0)
print(df2)

# a = pd.read_excel("battledeath.xlsx",sheet_name=None)
# print(a)  # you can specify your sheet of interest or it can give all of it by passing a dict
