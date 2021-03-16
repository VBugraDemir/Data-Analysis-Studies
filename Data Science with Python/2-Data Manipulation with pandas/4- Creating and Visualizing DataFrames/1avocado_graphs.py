# Histogram distribution of numeric data
# Bar plot can reveal the relationships between a categorical variable and a numeric variable
# Line plots are designed to visualize the relationship between two numeric variables, where each data values is
# connected to the next one.
# Scatter plot are great for visualizing relationships between two numeric variables.
import matplotlib.pyplot as plt

import pickle
import pandas as pd
newfile = open("avoplotto.pkl","rb")
avocados = pickle.load(newfile)
print(avocados.head())

# bar plot
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
nb_sold_by_size.plot(kind = "bar")
plt.show()

# nb_sold_by_size = avocados.groupby("size").sum()
# nb_sold_by_size.plot(kind = "bar", y ="nb_sold")
# plt.show()

# line plot
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
nb_sold_by_date.plot(kind = "line")
plt.show()

# scatter plot
avocados.plot(x = "nb_sold", y = "avg_price", kind = "scatter", title = "Number of avocados sold vs. average price")
plt.show()

# price of conventional vs. organic avocados
avocados[avocados["type"] == "conventional"]["avg_price"].hist(bins = 20, alpha = 0.5)
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins = 20, alpha = 0.5)
plt.legend(["conventional","organic"])
plt.show()
