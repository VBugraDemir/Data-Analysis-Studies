import pickle
import pandas as pd
newfile = open("licenses.p","rb")
licenses = pickle.load(newfile)

newfile2 = open("zip_demo.p","rb")
zip_demo = pickle.load(newfile2)

newfile3 = open("ward.p","rb")
wards = pickle.load(newfile3)

licenses_zip_ward = licenses.merge(zip_demo, on = "zip") \
    .merge(wards, on = "ward")
print(licenses_zip_ward.groupby("alderman").agg({"income":"median"}))
