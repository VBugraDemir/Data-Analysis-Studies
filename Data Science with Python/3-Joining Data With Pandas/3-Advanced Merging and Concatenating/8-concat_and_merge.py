import pandas as pd
classic_18 = pd.read_csv("classic_18.csv", index_col= 0)
classic_19 = pd.read_csv("classic_19.csv", index_col= 0)
pop_18 = pd.read_csv("pop_18.csv", index_col= 0)
pop_19 = pd.read_csv("pop_19.csv", index_col= 0)

classic_18_19 = pd.concat([classic_18, classic_19], ignore_index= True)
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index= True)

classic_pop = classic_18_19.merge(pop_18_19, on = "tid")
popular_classic = classic_18_19[classic_18_19["tid"].isin(classic_pop["tid"])]
print(popular_classic)