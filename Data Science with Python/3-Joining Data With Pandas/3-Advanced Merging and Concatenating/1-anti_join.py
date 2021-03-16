import pandas as pd
# we need to see which employee is available
top_cust = pd.read_csv("top_cust.csv", index_col=0)
employees = pd.read_csv("employees.csv", index_col=0)

empl_cust = employees.merge(top_cust, on = "srid", how= "left", indicator=True)

srid_list = empl_cust.loc[empl_cust["_merge"] == "left_only"]
print(employees[employees["srid"].isin(srid_list["srid"])])