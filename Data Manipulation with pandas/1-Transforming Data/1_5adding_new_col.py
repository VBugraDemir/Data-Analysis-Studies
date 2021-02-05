import pickle
import pandas as pd
newfile = open("homeless_data.pkl","rb")
homelessness = pickle.load(newfile)
# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]
print(homelessness.head())