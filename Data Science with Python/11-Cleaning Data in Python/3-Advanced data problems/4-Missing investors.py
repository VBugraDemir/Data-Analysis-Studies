import pandas as pd

#  you need to make sure that all dates are of the same format
#  You will do so by converting this column into a datetime object,
#  while making sure that the format is inferred and potentially incorrect formats are set to missing.

banking = pd.read_csv("banking_dirty.csv", index_col=0, chunksize=97)
banking = next(banking)

banking = banking.drop("Age",axis=1)
banking = banking.drop("inv_amount",axis=1)

ages = pd.read_csv("ages.csv", index_col=0)
inv = pd.read_csv("inv_amounts.csv", index_col=0)

banking = banking.join([ages, inv])

print(banking.isna().sum())

import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(banking)
plt.show()

missing_investors = banking[banking["inv_amount"].isna()]
investors = banking[~banking["inv_amount"].isna()]

print(missing_investors.describe())
print(investors.describe())

banking_sorted = banking.sort_values("age")
msno.matrix(banking_sorted)
plt.show()
