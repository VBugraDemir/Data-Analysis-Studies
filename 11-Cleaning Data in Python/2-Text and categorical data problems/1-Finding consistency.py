# dropping out the inconsistent values from the table in a anti join inner join mindset.

import pandas as pd

airlines = pd.read_csv("airlines_final_unacceptable.csv", index_col=0)
categories = pd.read_csv("categories.csv", index_col=0)

# Print unique values of survey columns in airlines
print("Cleanliness:", airlines["cleanliness"].unique(), "\n")
print("Safety:", airlines["safety"].unique(), "\n")
print("Satisfaction:", airlines["satisfaction"].unique(), "\n")

cat_clean = set(airlines["cleanliness"]).difference(categories["cleanliness"])
print("the inconsistent values: ", cat_clean)

# Print rows with inconsistent category
cat_clean_row = airlines["cleanliness"].isin(cat_clean)
print(airlines[cat_clean_row])

# Print rows with consistent categories only
print(airlines[~cat_clean_row])
