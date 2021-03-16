import pandas as pd

ride_sharing = pd.read_csv("ride_sharing_new.csv", index_col=0)



tire_sizes= pd.read_csv("a.csv",index_col=0)
tire_sizes["tire_sizes"] = tire_sizes["tire_sizes"].astype("category")

ride_sharing=ride_sharing.join(tire_sizes)
print(ride_sharing)
print(ride_sharing.info())
ride_sharing["tire_sizes"] = ride_sharing["tire_sizes"].astype("int")
print(ride_sharing.info())
ride_sharing.loc[ride_sharing["tire_sizes"] > 27, "tire_sizes"] = 27
print(ride_sharing)
ride_sharing["tire_sizes"] = ride_sharing["tire_sizes"].astype("category")

print(ride_sharing["tire_sizes"].describe())
print(ride_sharing.info())
