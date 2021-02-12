import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

palette_colors = {"Rural":"green", "Urban":"blue"}

sns.countplot(x="school", hue="location", palette=palette_colors, data=student_data)
plt.show()
