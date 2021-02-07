import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv("young-people-survey-responses.csv", index_col=0)

survey_data["Likes Techno"] = [True if i >=4 else False for i in survey_data["Techno"]]

sns.set_style("dark")

g = sns.catplot(x="Village - town", y="Likes Techno", data=survey_data, kind="bar", col="Gender")
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel= "Location of Residence", ylabel="% Who like Techno")
plt.show()
