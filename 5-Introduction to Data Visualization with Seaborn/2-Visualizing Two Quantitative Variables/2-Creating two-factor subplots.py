import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

sns.relplot(x="G1", y="G3", data=student_data, kind="scatter",
            col="schoolsup", col_order=["yes", "no"], row="famsup", row_order=["yes", "no"])
plt.show()
# correlation exists so support has no impact there
