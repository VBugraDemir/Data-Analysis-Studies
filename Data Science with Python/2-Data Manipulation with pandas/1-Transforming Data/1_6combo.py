import pickle
import pandas as pd
newfile = open("homeless_data.pkl","rb")
homelessness = pickle.load(newfile)
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"]/ homelessness["state_pop"]
high_homelessness = homelessness[homelessness["indiv_per_10k"]>20]
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k",ascending = False)
result = high_homelessness_srt[["state","indiv_per_10k"]]
print(result)