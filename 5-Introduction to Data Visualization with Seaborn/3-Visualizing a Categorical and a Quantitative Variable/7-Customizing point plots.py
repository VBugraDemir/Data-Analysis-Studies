# Point plots show the mean of a quantitative variable for the observations
# in each category

# point plot vs. line plot
# they both show the mean of a quantitative variable but line plots are relational plots
# so x and y axis are quantitative, but x axis of point plots is categorical

# point plot vs. bar plot
# they also show the mean of a quantitative variable.
# but making comparisons is easier with point plots

# vertical bars represent the 95% confidence intervals for the mean

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)
print(student_data.groupby("famrel")["absences"].mean())
sns.catplot(x="famrel", y="absences", data=student_data, kind="point", capsize=0.2, join=False)

sns.catplot(x="famrel", y="absences", data=student_data, kind="bar")
plt.show()