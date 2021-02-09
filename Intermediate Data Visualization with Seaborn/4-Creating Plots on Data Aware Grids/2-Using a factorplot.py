import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tuitions.csv")

sns.factorplot(data=df, row="Degree_Type", kind="box", x="Tuition")
plt.show()

# g=sns.FacetGrid(df, row="Degree_Type")
# g.map(sns.boxplot, "Tuition")
# plt.show()

# sns.catplot(data=df, row="Degree_Type", kind="box", x="Tuition")
# plt.show()
# faceting can be done by using catplots too


sns.factorplot(data=df, x="SAT_AVG_ALL", kind="point", row="Degree_Type", row_order = ['Graduate', 'Bachelors', 'Associates', 'Certificate'])
plt.show()
