import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)

store_types = sales.drop_duplicates(["store","type"])

store_depts = sales.drop_duplicates(["store","department"])

store_counts = store_types["type"].value_counts()
print(store_counts)

store_props = store_types["type"].value_counts(normalize = True)
print(store_props)

dept_counts_sorted = store_depts["department"].value_counts(sort = True)
print(dept_counts_sorted)

dept_props_sorted = store_depts["department"].value_counts(sort=True,normalize = True)
print(dept_props_sorted)