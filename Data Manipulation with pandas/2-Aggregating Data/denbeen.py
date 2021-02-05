import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)
pd.set_option("display.max_columns", None)
print(sales)
new_sales = sales[["weekly_sales","fuel_price_usd_per_l"]]
print(type(new_sales))
print(new_sales.mean(axis ="columns"))

