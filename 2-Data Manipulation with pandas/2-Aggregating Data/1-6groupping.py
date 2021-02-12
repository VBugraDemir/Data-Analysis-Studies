import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)
# not using .groupby

sales_all = sales["weekly_sales"].sum()

sales_a = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_b = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_c = sales[sales["type"] == "C"]["weekly_sales"].sum()

sales_probn_by_type = [sales_a,sales_b,sales_c] / sales_all
print(sales_probn_by_type)

# using .grupby
sales_by_type = sales.groupby("type")["weekly_sales"].sum()  # or .agg()
sales_probn_by_type = sales_by_type/sales_by_type.sum()
print(sales_probn_by_type)

# also by using pivot table
import numpy as np
mean_sales = sales.pivot_table(values = "weekly_sales", index = "type", aggfunc = np.sum)
print(mean_sales)

# If no function specified it takes the mean of the values
mean_sales = sales.pivot_table(values = "weekly_sales", index = "type")
print(mean_sales)

sales_by_type_is_holiday = sales.groupby(["type","is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# multiple groupping
import numpy as np
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min,np.max,np.mean,np.median])
print(sales_stats)
pd.set_option("display.max_columns",None)
unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]].agg([np.min,np.max,np.mean,np.median])
print(unemp_fuel_stats)
print(sales[sales["weekly_sales"] == -4988.94])

