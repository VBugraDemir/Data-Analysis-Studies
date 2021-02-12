import pandas as pd

url = "http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls"

xls = pd.read_excel(url, sheet_name=None)
print(xls.keys())
print(xls["1700"].head())
