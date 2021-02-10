import pandas as pd
import matplotlib.pyplot as plt
from sas7bdat import SAS7BDAT

with SAS7BDAT("sales.sas7bdat") as file:
    df_sas = file.to_data_frame()
print(df_sas.head())
# df_sas = pd.read_sas("sales.sas7bdat")
# print(df_sas.head())

pd.DataFrame.hist(df_sas[["P"]])  # df_sas["P"].hist()
plt.ylabel("count")
plt.show()
