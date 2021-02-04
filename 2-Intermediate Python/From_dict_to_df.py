# The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular
# data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.
import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict = { "country":names, "drives_right":dr, "cars_per_cap":cpc}
print(my_dict)
cars = pd.DataFrame(my_dict)
print(cars)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)

