import pandas as pd
import datetime as dt
ride_sharing = pd.read_csv("ride_sharing_new.csv", index_col=0)


ride_dates= pd.read_csv("dates.csv",index_col=0)
# ride_dates["ride_date"] = ride_dates["ride_date"].astype("str")

ride_sharing = ride_sharing.join(ride_dates)
print(ride_sharing["ride_date"].max())
ride_sharing["ride_dt"] = pd.to_datetime(ride_sharing["ride_date"])  # datacampte bu  yoktu  ama
# date ile datetime64 ü karşılaştırmama izin vermedi.
# or ride_sharing["ride_dt"] = pd.to_datetime(ride_sharing["ride_date"]).dt.date
# but the data type changes from datetime to object.
today = dt.datetime.today()


ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

print(ride_sharing["ride_dt"].max())
