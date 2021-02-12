import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# residual plot is useful for evaluating the fit of a model

tuition = pd.read_csv("tuitions.csv")

sns.regplot(data=tuition, x="SAT_AVG_ALL", y="Tuition", marker="^", color="g")
plt.show()

sns.residplot(data=tuition, x="SAT_AVG_ALL", y="Tuition", color="g")
plt.show()
# There does appear to be a linear relationship between tuition and SAT scores.
