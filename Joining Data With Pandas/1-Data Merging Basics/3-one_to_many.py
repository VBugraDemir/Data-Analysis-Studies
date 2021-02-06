import pickle
import pandas as pd
newfile = open("licenses.p","rb")
licenses = pickle.load(newfile)
newfile2 = open("business_owners.p","rb")
biz_owners = pickle.load(newfile2)

licenses_owners = licenses.merge(biz_owners, on = "account")

# counted_df = licenses_owners.groupby("title")
# print(counted_df["account"].count())
counted_df = licenses_owners.groupby("title").agg({"account":"count"})  # accounts are counted in a dict, more than one calculations can be in a list...
print(counted_df.sort_values("account", ascending= False))

