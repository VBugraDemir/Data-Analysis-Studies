import pandas as pd
inv_feb_list = {
    "cid":[38, 40, 42],
    "invoice_date":["209-02-01", "209-02-01", "209-02-02"],
    "total":[1.98, 1.98, 3.96]
}
iid = [7, 8, 9]
inv_feb = pd.DataFrame(inv_feb_list, index= iid)

inv_mar_list = {
    "cid":[17, 19, 21],
    "invoice_date":["209-03-04", "209-03-04", "209-03-05"],
    "total":[1.98, 1.98, 3.96]
}
iid = [9, 15, 16]
inv_mar = pd.DataFrame(inv_mar_list, index= iid)

# pd.concat([inv_feb, inv_mar], verify_integrity= True) # error is raised because there is an overlapping value
print(pd.concat([inv_feb, inv_mar], verify_integrity= False))
# real world data is often not clean so we need to check that
# we need to fix incorrect data and drop duplicate rows
