import pandas as pd
airline_bumping = pd.read_csv("airline_bumping.csv")

print(airline_bumping.head())

airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
print(airline_totals)

# DF to csv file
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k",ascending = False)
print(airline_totals_sorted)

airline_totals_sorted.to_csv("airline_totals_sorted.csv")