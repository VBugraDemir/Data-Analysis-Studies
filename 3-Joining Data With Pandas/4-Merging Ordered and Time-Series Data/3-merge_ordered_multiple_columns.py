# merge_ordered has fill_method = "ffill"
import pandas as pd

gdp = pd.read_csv("gdp_china_us.csv", index_col= 0)
pop = pd.read_csv("pop.csv", index_col= 0)

date_country = pd.merge_ordered(gdp, pop, on = ["date", "country"], fill_method="ffill")
print(date_country) # we keep assigning pop of the us to china

country_date = pd.merge_ordered(gdp, pop, on = ["country", "date"], fill_method="ffill")
print(country_date)

# The fill forward is using unintended data to fill in the missing values.
# However, when you merge on country first, the table is sorted by country then date,
# so the forward fill is applied appropriately in this situation.
