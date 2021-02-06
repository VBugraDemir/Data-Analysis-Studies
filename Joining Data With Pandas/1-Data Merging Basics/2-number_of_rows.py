import pickle
import pandas as pd
newfile = open("ward.p","rb")
wards = pickle.load(newfile)
newfile2 = open("census.p","rb")

# one-to-one relationship

census = pickle.load(newfile2)
wards_census = wards.merge(census, on = "ward")
print(wards_census.shape)

wards.loc[wards["ward"] == "1", "ward"] = "61"
wards_census = wards.merge(census, on = "ward")
print(wards_census.shape)

wards.loc[wards["ward"] == "61", "ward"] = None
wards_census = wards.merge(census, on = "ward")
print(wards_census.shape)