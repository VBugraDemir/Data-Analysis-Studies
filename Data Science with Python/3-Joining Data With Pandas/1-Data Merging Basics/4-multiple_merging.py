import pickle
import pandas as pd
newfile = open("cta_ridership.p","rb")
ridership = pickle.load(newfile)

newfile2 = open("cta_calendar.p","rb")
cal = pickle.load(newfile2)

newfile3 = open("stations.p","rb")
stations = pickle.load(newfile3)

ridership_cal_stations = ridership.merge(cal, on = ["year", "month", "day"]).merge(stations, on = "station_id")
filter_criteria = ((ridership_cal_stations["month"] == 7) & (ridership_cal_stations["day_type"] == "Weekday") &
                   (ridership_cal_stations["station_name"] == "Wilson"))
print(ridership_cal_stations.loc[filter_criteria, "rides"].sum())
print(ridership_cal_stations[filter_criteria]["rides"].sum())
