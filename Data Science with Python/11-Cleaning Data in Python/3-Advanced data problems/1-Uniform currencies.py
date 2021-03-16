import pandas as pd

banking = pd.read_csv("banking_dirty.csv", index_col=0, chunksize=97)
banking = next(banking)
cur = pd.read_csv("cur.csv", index_col=0)

banking = banking.join(cur)
print(banking[["acct_amount", "acct_cur"]])

acct_eu = banking["acct_cur"] == "euro"
banking.loc[acct_eu, "acct_amount"] = banking.loc[acct_eu, "acct_amount"] * 1.1
banking.loc[acct_eu, "acct_cur"] = "dollar"
print(banking[["acct_amount", "acct_cur"]])