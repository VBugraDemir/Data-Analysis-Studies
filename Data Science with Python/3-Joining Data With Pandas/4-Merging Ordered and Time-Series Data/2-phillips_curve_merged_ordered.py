import matplotlib.pyplot as plt
import pandas as pd
unemployment = pd.read_csv("unemployment.csv", index_col= 0)
inflation = pd.read_csv("inflation.csv", index_col= 0)

inflation_unemploy = pd.merge_ordered(inflation, unemployment, on = "date", how= "inner")
print(inflation_unemploy)
inflation_unemploy.plot(kind = "scatter", x="unemployment_rate", y="cpi")
plt.show()
