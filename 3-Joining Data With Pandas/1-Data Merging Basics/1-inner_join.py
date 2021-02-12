import pickle
import pandas as pd
newfile = open("taxi_owners.p","rb")
taxi_owners = pickle.load(newfile)

newfile2 = open("taxi_vehicles.p","rb")
taxi_vehicles = pickle.load(newfile2)

# inner joins only return the rows with matching values in both tables
taxi_own_veh = taxi_owners.merge(taxi_vehicles, on = "vid")
print(taxi_own_veh.columns)  # so there is _x and _y column names we can fix it

taxi_own_veh = taxi_owners.merge(taxi_vehicles, on = "vid", suffixes = ["_own", "_veh"])
print(taxi_own_veh.columns)

# to see the most used fuel type
print(taxi_own_veh["fuel_type"].value_counts())
print(taxi_vehicles.columns)
print(taxi_owners.columns)