import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

# we'll add subgroups based on where the student lives. For this, we can use the "location" variable

sns.catplot(x="internet", y="G3", data=student_data, kind="box", hue="location", sym="")
plt.show()
