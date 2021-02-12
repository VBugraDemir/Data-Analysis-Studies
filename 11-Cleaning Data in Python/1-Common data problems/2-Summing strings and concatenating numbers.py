import pandas as pd

ride_sharing = pd.read_csv("ride_sharing_new.csv", index_col=0)
print(ride_sharing[["duration"]])
ride_sharing['duration_trim'] = ride_sharing["duration"].str.strip("minutes")
ride_sharing["duration_time"] = ride_sharing["duration_trim"].astype("int")
assert ride_sharing["duration_time"].dtype == "int"

print(ride_sharing[["duration", "duration_trim", "duration_time"]])
print(ride_sharing["duration_time"].mean())
