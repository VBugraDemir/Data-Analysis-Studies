import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("young-people-survey-responses.csv", index_col=0)

sns.countplot(x="Spiders", data=df)
plt.show()
#sns.countplot(x=df["Spiders"])
# plt.show()

# df["Spiders"].value_counts().plot(kind="bar")
# plt.show()
