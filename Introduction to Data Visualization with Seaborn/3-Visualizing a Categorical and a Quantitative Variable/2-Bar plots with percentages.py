# categorical variable to put on the x-axis (x=____),
# the name of the quantitative variable to summarize on the y-axis (y=____)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)
survey_data["Interested in Math"] = [True if i > 3 else False for i in survey_data["Mathematics"]]
# print(survey_data[["Mathematics", "Interested in Math"]])
print(survey_data["Interested in Math"])
sns.catplot(x="Gender", y="Interested in Math", data=survey_data, kind="bar")
plt.show()

# When the y-variable is True/False, bar plots will show the percentage of responses reporting True.
