import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)
print(student_data.groupby("study_time")["G3"].mean())
sns.catplot(x="study_time", y="G3", data=student_data, kind="bar",
            order=["<2 hours", "2 to 5 hours",
                   "5 to 10 hours", ">10 hours"], ci=None)
plt.show()
