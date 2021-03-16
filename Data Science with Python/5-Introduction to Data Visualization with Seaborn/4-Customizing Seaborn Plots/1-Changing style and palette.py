import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)

category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
survey_data["Parents Advice"] = ["Never" if i==1.0 else "Rarely"  if i==2.0 else "Sometimes" if i==3.0 else "Often" if i==4.0 else "Always" for i in survey_data["Parents' advice"]]

sns.set_style("whitegrid")
sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)
# plt.show()

sns.set_style("whitegrid")
sns.set_palette("Purples")
sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)
# plt.show()

sns.set_style("whitegrid")
sns.set_palette("RdBu")
sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)
plt.show()

