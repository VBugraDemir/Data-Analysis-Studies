import pandas as pd
social_fin = pd.read_csv("social_fin.csv", index_col=0)
print(social_fin.query('value > 50000000'))
print()
print(social_fin.query('financial == "total_revenue" and company == "facebook"'))
print()
print(social_fin.query('financial == "net_income" and value < 0'))
print()
print(social_fin.query('financial == "gross_profit" and value > 100000'))