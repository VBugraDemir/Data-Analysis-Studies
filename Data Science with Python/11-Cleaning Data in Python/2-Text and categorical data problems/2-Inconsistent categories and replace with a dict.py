
import pandas as pd

airlines = pd.read_csv("airlines_final_unacceptable.csv", index_col=0)

# there are some problems with these values such as unnecessary whitespaces and capitalized letters.
print(airlines["dest_region"].unique())
print(airlines["dest_size"].unique(), "\n")

airlines["dest_region"] = airlines["dest_region"].str.lower()
airlines["dest_region"] = airlines["dest_region"].replace({"eur":"europe"})
print(airlines.info())
airlines["dest_size"] = airlines["dest_size"].str.strip()

print(airlines["dest_region"].unique())
print(airlines["dest_size"].unique())