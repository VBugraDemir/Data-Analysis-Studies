import pandas as pd

csv1 = pd.read_csv("csv1.csv", index_col=0)
csv2 = pd.read_csv("csv2.csv", index_col=0)
csv3 = pd.read_csv("csv3.csv", index_col=0)
csv4 = pd.read_csv("csv4.csv", index_col=0)
df = csv1.join([csv2,csv3,csv4])

duplicates = df.duplicated(subset="ride_id", keep=False)
duplicated_rides = df[duplicates]
print(duplicated_rides[["ride_id", "duration", "user_birth_year"]])

ride_dub = df.drop_duplicates()
print(ride_dub)
duplicates = ride_dub.duplicated(subset="ride_id", keep=False)
duplicated_rides = ride_dub[duplicates]
print(duplicated_rides[["ride_id", "duration", "user_birth_year"]])

statistics = {"user_birth_year":"min","duration":"mean"}
ride_unique = ride_dub.groupby("ride_id").agg(statistics).reset_index()
print(ride_unique)

duplicates = ride_unique.duplicated(subset="ride_id", keep=False)
duplicated_rides = ride_unique[duplicates]
assert duplicated_rides.shape[0] == 0
