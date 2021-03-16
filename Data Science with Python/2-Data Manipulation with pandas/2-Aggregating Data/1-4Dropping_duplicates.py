import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)

store_types = sales.drop_duplicates(["store","type"])
print(store_types.head())

store_depts = sales.drop_duplicates(["store","department"])
print(store_depts)

# store_depts = sales.drop_duplicates(subset = ["store","department"])
# print(store_depts)
holiday_dates = sales[sales["is_holiday"]].drop_duplicates("date")
print(holiday_dates)
