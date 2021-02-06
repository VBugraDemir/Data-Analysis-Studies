# This method can merge time series and other ordered data.
import pandas as pd
sp500 = pd.read_csv("S&P500.csv")
# sp500["Date"] = sp500["Date"].astype("int64")

gdp = pd.read_csv("WorldBank_GDP.csv")
gdp = gdp[gdp["Country Code"] == "USA"][["Country Code","Year", "GDP"]]
print(gdp)
# print(gdp.loc[gdp["Country Code"] == "USA",["Country Code","Year","GDP"]]) the same thing with the previous one.

gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on= "Year", right_on= "Date", how="left")
print(gdp_sp500)
print()
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on= "Year", right_on= "Date", how="left", fill_method= "ffill")
print(gdp_sp500)

# subsetting

gdp_returns = gdp_sp500[["GDP", "Returns"]]
print(gdp_returns.corr())
# the correlation of 0.21 between the GDP and S&P500 is low to moderate at best.
# You may want to find another predictor if you plan to play in the stock market.
