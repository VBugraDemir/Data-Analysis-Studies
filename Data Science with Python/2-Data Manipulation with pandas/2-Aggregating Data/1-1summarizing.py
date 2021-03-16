import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)
print(sales.head())
print()
print(sales.info())
print()
print(sales["weekly_sales"].mean())
print()
print(sales["weekly_sales"].median())
# mean ile median arasındaki ilişki ilgi çekici. İki katından daha fazla...
# tarihlerin data type'ı datetime64

print(sales["date"].max())
print(sales["date"].min())


