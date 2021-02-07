# the relationship between two quantitative variables -> relational plots
# scatter and lineplots

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)
# creating separate plot per subgroup by useing relplot

sns.relplot(x="absences", y="G3", data=student_data, kind="scatter", col="study_time")
plt.show()

sns.relplot(x="absences", y="G3", data=student_data, kind="scatter", row="study_time")
plt.show()
