import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv("student-alcohol-consumption.csv", index_col=0)

sns.catplot(x="romantic", y="G3", data=student_data, kind="box")
plt.show()

sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=0.5)
plt.show()

sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=[5, 95])
plt.show()

sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=[0, 100])
plt.show()
