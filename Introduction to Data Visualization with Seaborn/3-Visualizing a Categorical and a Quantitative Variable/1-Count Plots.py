# count plots and bar plots are two types of visualizations that seaborn calls "categorical" plots
# categorical plots involve categorical variable that is fixed, small number of possible values or
# categories.
# these plots are used when we want to make comparisons between different groups.
#
# count plot is a kind of categorical plots
# bar plots show the mean of the observation in each category.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)
survey_data["Age Category"] = ["Less than 21" if i < 21 else "21+" for i in survey_data["Age"]]  # manipulated column xd

sns.catplot(x="Internet usage", data=survey_data, kind="count")
plt.show()

sns.catplot(y="Internet usage", data=survey_data, kind="count")
plt.show()

sns.catplot(y="Internet usage", data=survey_data, kind="count", col="Age Category")
plt.show()
