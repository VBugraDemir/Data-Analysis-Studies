import pandas as pd
cars =pd.read_csv("cars.csv", index_col =0)
for lab, row in cars.iterrows():
    print(lab)
    print(row)
print("\n")
for lab, row in cars.iterrows():
    print(lab+": "+row["capital"])

# an inefficient way to add column to a data frame is iterating every row
# first one is the row label the second is the row data.
for lab, row in cars.iterrows():
    cars.loc[lab,"name_lengts_for"] = len(row["country"]) # creating neme lengths column for every label(row)
print(cars,"\n")
# loc and iloc first names of the rows and then the columns.
# here row holds the data we can reach any data by typing the name of the column

# the efficient and the better way to do it is using the apply() without any for loops.
# ****applying a function on a particular column in an element-wise fashion
cars["name_length_apply"] = cars["country"].apply(len)
print(cars)
