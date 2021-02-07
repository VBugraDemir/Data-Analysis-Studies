import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)

sns.set_style("darkgrid")
sns.set_palette(["#39A7D0", "#36ADA4"])
sns.catplot(x="Gender", y="Age", data=survey_data, kind="box")
plt.show()
