import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)
survey_data["Interested in Pets"] = ["Yes" if i>=4 else "No" for i in survey_data["Pets"]]

sns.set_palette("Blues")
g = sns.catplot(x="Gender", y="Age", data=survey_data, kind="box", hue="Interested in Pets")
g.fig.suptitle("Age of Those Interested in Pets vs. Not")
plt.show()