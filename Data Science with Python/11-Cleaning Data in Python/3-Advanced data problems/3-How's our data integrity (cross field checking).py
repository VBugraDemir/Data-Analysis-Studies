import pandas as pd
import datetime as dt

banking = pd.read_csv("banking_dirty.csv", index_col=0)

fund_columns = ["fund_A", "fund_B", "fund_C", "fund_D"]
inv_equ = banking[fund_columns].sum(axis=1) == banking["inv_amount"]
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]
print("Number of inconsistent investments:",inconsistent_inv.shape[0])


banking["birth_date"] = pd.to_datetime(banking["birth_date"])
today = dt.date.today()

ages_manual = today.year - banking["birth_date"].dt.year


age_equ = banking["Age"] == ages_manual
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]
print("Number of inconsistent ages:", inconsistent_ages.shape[0])
