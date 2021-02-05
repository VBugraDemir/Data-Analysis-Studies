# from a list of dictionaries (row by row) and
# from a dictionary of lists (column by column)
import pandas as pd

# list of dictionaries
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

avocados_2019 = pd.DataFrame(avocados_list)
print(avocados_2019)

# dictionary of lists
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}
avocados_2019_2 = pd.DataFrame(avocados_dict)
print(avocados_2019_2)

