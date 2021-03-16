import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tuitions.csv")

g2 = sns.FacetGrid(df, row="Degree_Type", row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

g2.map(sns.pointplot, "SAT_AVG_ALL")
plt.show()
