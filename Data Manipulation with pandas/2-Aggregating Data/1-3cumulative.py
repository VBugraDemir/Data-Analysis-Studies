import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)

sales_1_1 = sales.sort_values("date")
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
print(sales_1_1[["date","weekly_sales","cum_weekly_sales","cum_max_sales"]])