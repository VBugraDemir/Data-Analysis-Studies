import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tuitions.csv")

g = sns.FacetGrid(df, col = "Degree_Type", col_order=['Graduate', 'Bachelors', 'Associates'])
g.map(plt.scatter, "UG", "PCTPELL")
plt.show()

sns.lmplot(data=df, x="UG", y="PCTPELL", col="Degree_Type", col_order=['Graduate', 'Bachelors', 'Associates'])
plt.show()

sns.lmplot(data=df, x="SAT_AVG_ALL", y="Tuition", col="Ownership", row="Degree_Type", row_order=['Graduate', 'Bachelors'],
           hue="WOMENONLY", col_order=['Public', 'Private non-profit'])
plt.show()
