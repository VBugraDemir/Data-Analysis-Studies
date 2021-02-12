import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")

g=sns.relplot(x="model_year", y="mpg", data=mpg,kind="line", hue="origin",ci=None)
g.fig.suptitle("Average MPG Over Time")
g.set(xlabel="Car Model Year", ylabel="Average MPG")
plt.show()

mpg_mean = mpg.groupby(["model_year", "origin"], as_index=False)["mpg"].mean()

g=sns.lineplot(x="model_year", y="mpg", data=mpg_mean, hue="origin")
g.set_title("Average MPG Over Time")
g.set(xlabel="Car Model Year", ylabel="Average MPG")
plt.show()
