import pandas as pd

ride_sharing = pd.read_csv("ride_sharing_new.csv", index_col=0)
print(ride_sharing[["user_type"]])
print(ride_sharing.info())

# in dataframe user type is  actually in a categorical type but here it is int
print(ride_sharing["user_type"].describe())
# so describe is misleading

ride_sharing["user_type"] = ride_sharing["user_type"].astype("category")
assert ride_sharing["user_type"].dtype == "category"
print(ride_sharing["user_type"].describe())
print(ride_sharing.groupby("user_type")["user_type"].count())

