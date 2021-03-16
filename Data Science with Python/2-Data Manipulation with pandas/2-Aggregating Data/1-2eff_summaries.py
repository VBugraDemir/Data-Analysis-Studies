import pickle
import pandas as pd
newfile = open("walmart_sales.pkl","rb")
sales = pickle.load(newfile)

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

print(sales["temperature_c"].agg(iqr))
print(sales[["temperature_c","fuel_price_usd_per_l","unemployment"]].agg(iqr))

import numpy as np
print(sales[["temperature_c","fuel_price_usd_per_l","unemployment"]].agg([iqr,np.median]))
