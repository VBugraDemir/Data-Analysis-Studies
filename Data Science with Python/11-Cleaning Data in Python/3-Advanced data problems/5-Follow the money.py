import pandas as pd

banking = pd.read_csv("banking_dirty.csv", index_col=0, chunksize=97)
banking = next(banking)
banking = banking.drop(["cust_id","acct_amount"], axis=1)
# banking = banking.drop("acct_amount", axis=1)

cust_id = pd.read_csv("cust_id.csv", index_col=0)
act_amount = pd.read_csv("acct_amount.csv", index_col=0)

banking = banking.join(cust_id)
banking = banking.join(act_amount)

print(banking.isna().sum())

banking_fullid = banking.dropna(subset =["cust_id"])
print(banking_fullid[banking_fullid["acct_amount"].isna()])

compare = banking_fullid[banking_fullid["acct_amount"].isna()]["cust_id"].values
acct_imp = banking_fullid["inv_amount"] * 5

banking_imputed = banking_fullid.fillna({"acct_amount":acct_imp})
print(banking_imputed[banking_imputed["cust_id"].isin(compare)])
print(banking_imputed.isna().sum())
#


