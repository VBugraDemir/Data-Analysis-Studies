import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

sns.scatterplot(x="absences", y="G3", hue="location", data=student_data)
plt.show()

sns.scatterplot(x="absences", y="G3", hue="location", hue_order=["Rural", "Urban"], data=student_data)
plt.show()
