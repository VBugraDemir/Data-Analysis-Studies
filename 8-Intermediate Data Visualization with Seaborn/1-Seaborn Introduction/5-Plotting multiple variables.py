import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv("insurance.csv")

sns.lmplot(x="insurance_losses", y="premiums", data=insurance, rows="Region")
plt.show()

# The results are bit difficult to read. Maybe using multiple lines is not the best approach
