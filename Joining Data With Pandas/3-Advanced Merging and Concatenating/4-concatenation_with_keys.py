# given three tables with invoice data named inv_jul, inv_aug, and inv_sep
import matplotlib.pyplot as plt
import pandas as pd

inv_jul = pd.read_csv("inv_jul.csv")
inv_sep = pd.read_csv("inv_sep.csv")
inv_aug = pd.read_csv("inv_aug.csv")

inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], keys=["7Jul", "8Aug", "9Sep"])
print(inv_jul_thr_sep)
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({"total":"mean"})
print(avg_inv_by_month)
avg_inv_by_month.plot(kind="bar")
plt.show()


# Group the invoices by the index keys and find avg of the total column
# avg_inv_by_month = inv_jul_thr_sep.groupby(level = 0).agg({"total":"mean"})
# avg_inv_by_month.plot(kind = "bar")
# ply.show()
