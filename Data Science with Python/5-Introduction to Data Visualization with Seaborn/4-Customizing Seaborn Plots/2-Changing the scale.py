import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Changing the scale of the plot for a kind of a presentation

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)


survey_data["Number of Siblings"] = ["0" if i==0 else "3+" if i>=3 else "1 - 2" for i in survey_data["Siblings"]]
survey_data["Feels Lonely"] = [False if i<=3 else True for i in survey_data["Loneliness"]]
# Since the values are Trues and falses the bar plat will take the percentage of True values.
order = ["0", "1 - 2", "3+"]

sns.set_context("paper")
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar", order=order)
plt.show()

sns.set_context("notebook")
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar", order=order)
plt.show()

sns.set_context("talk")
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar", order=order)
plt.show()

sns.set_context("poster")
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar", order=order)
plt.show()
