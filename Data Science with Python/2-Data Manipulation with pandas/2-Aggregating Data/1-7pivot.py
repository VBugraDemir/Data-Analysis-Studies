import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)

# Pivot tables are the standard way of aggregating data in spreadsheets. In pandas,
# pivot tables are essentially just another way of performing grouped calculations.

mean_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type")
print(mean_sales_by_type)

# mean_sales_by_type = sales.groupby("type")["weekly_sales"].mean()
# print(mean_sales_by_type)

import numpy as np
mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type",aggfunc=[np.mean,np.median])
print(mean_med_sales_by_type)

mean_sales_by_type_holiday = sales.pivot_table(values = "weekly_sales", index= "type", columns = "is_holiday")
print(mean_sales_by_type_holiday)

# filling the missing values
pd.set_option("display.max_rows",None)
print(sales.pivot_table(values = "weekly_sales",index = "department",columns = "type", fill_value=0))
print(sales.pivot_table(values = "weekly_sales", index = "department", columns ="type", fill_value=0, margins=True))
ase = sales.pivot_table(values = "weekly_sales",index = "department",columns = "type", fill_value=0)
print(ase.mean(axis="columns"))  # calculate statistics across the columns (for each row)
print(ase.mean(axis="index"))  # calculate statistics across the rows (for each col)
# for most dataframes setting the axis arg does not make any sense (dif data types in cols) but
# for pivot tables are a special case since every col contains the same data type
