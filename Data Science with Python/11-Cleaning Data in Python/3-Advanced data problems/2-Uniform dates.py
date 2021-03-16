import pandas as pd

#  you need to make sure that all dates are of the same format
#  You will do so by converting this column into a datetime object,
#  while making sure that the format is inferred and potentially incorrect formats are set to missing.

banking = pd.read_csv("banking_dirty.csv", index_col=0, chunksize=97)
banking = next(banking)
banking = banking.drop("account_opened", axis=1)

dates = pd.read_csv("dates.csv", index_col=0)

banking = banking.join(dates)
print(banking)
print(banking.info())

banking["account_opened"] = pd.to_datetime(banking["account_opened"],infer_datetime_format=True, errors="coerce")
print(banking)
print(banking.info())

banking["acct_year"] = banking["account_opened"].dt.strftime("%Y")
print(banking["acct_year"])