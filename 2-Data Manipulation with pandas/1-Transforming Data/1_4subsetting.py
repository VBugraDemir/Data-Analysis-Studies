import pickle
import pandas as pd
newfile = open("homeless_data.pkl","rb")
homelessness = pickle.load(newfile)

# subsetting columns

individuals = homelessness["individuals"]
print(individuals.head())
print()
ind_state = homelessness[["individuals","state"]]
print(ind_state.head())
print()

# subsetting rows

ind_gt_10k = homelessness[homelessness["individuals"]>10000]
print(ind_gt_10k)
print()

mountain_reg = homelessness[homelessness["region"]=="Mountain"]
print(mountain_reg)
print()

import numpy as np
fam_lt_1k_pac = homelessness[(homelessness["family_members"]<1000) & (homelessness["region"]=="Pacific")]
# fam_lt_1k_pac = homelessness[np.logical_and(homelessness["family_members"]<1000 , homelessness["region"]=="Pacific")]
print(fam_lt_1k_pac)

# Subsetting rows by categorical variables

south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]
print(south_mid_atlantic)
print()

# using .isin()
canu = ["California","Arizona","Nevada","Utah"]
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]
print(mojave_homelessness)
