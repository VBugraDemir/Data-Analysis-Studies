import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance = pd.read_csv("insurance.csv")

sns.pairplot(data=insurance,
        x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"],
        y_vars=['premiums', 'insurance_losses'],
        kind='scatter',
        hue='Region',
        palette='husl')

plt.show()


sns.pairplot(data=insurance,
        vars=['insurance_losses', 'premiums'],
        kind='reg',
        diag_kind="kde",
        hue='Region',
        palette="BrBG"
        )

plt.show()
