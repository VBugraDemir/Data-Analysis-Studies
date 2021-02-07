# A box plot shows the distribution of a quantitative data
# the box represent the 25th to 75th percentile, the line in the middle of the box
# represents the median, whiskers gives a sense of the spread of the distribution, and the
# floating points represents outliers

# it is used to compare the distribution of a quantitative variable across different groups of a categorical
# variable

# seaborn has already boxplot function but catplot is used because it makes it easy to create rows and
# columns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

study_time_order = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

sns.catplot(x="study_time", y="G3", data=student_data, kind="box", order=study_time_order)
plt.show()
