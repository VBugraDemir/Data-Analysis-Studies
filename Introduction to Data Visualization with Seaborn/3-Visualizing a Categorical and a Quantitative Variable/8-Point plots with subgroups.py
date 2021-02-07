import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school")
plt.show()

sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school", ci=None)
plt.show()

# Since there may be outliers of students with many absences, import the median function from numpy
# and display the median number of absences instead of the average.

sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school", estimator=median, ci=None)
plt.show()
