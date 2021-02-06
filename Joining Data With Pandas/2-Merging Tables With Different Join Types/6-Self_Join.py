import pickle
import pandas as pd
import matplotlib.pyplot as plt
newfile = open("crews.p","rb")
crews = pickle.load(newfile)
crews = crews[["id", "job", "name"]]
pd.set_option("display.max_columns", None)

crews_self_merged = crews.merge(crews, on = "id", suffixes = ["_dir", "_crew"])
boolean_filter = ((crews_self_merged["job_dir"] == "Director") & (crews_self_merged["job_crew"] != "Director"))
direct_crews = crews_self_merged[boolean_filter]
print(direct_crews)

