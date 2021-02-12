#####
# CSV file'ı data frame cevirme
####
import pandas as pd
cars =pd.read_csv("cars.csv", index_col =0)
print(cars)
print(type(cars))
print("\n")

print(cars[["country", "area", "population"]][cars["population"] > 200])

print(cars["country"])
print(type(cars["country"]))
print("\n")
print(cars[["country"]])
print(type(cars[["country"]]))
print("\n")

print(cars[["country","capital"]])
print("\n")

print(cars[1:4])
print(type(cars[1:4]))
print("\n")
# square brackets work but limited. to get rows and columns loc (label based) and loci (integer position based) can be used
# rows as pandas series
print(cars.loc["RU"])
print("\n")
# rows as pandas dataframe
print(cars.loc[["RU"]])
print("\n")

# iloc index 1 is used
print("asddddddddddddd")
print(cars.iloc[:,[2]])
print("\n")

print(cars.loc[["RU","IN","CH"]])
print("\n")
print(cars.iloc[[1,2,3]])
print("\n")

#prints the intersection
print(cars.loc[["RU","IN","CH"],["country","capital"]])
print("\n")
print(cars.iloc[[1,2,3],[0,1]])
print("\n")
# to print the all rows
print(cars.loc[:,["country","capital"]])
print("\n")
# with cars.ix[[]] you can use indexes and labels together UPDATE it is removed
print(cars[cars.capital.isin(["Brasilia","Moscow"])])
# print(cars[cars["capital"]=="Brasilia"])
