import pandas as pd
import numpy as np

airlines = pd.read_csv("airlines_final_unacceptable.csv", index_col=0)

label_ranges = [0, 60, 180, np.inf]
label_names = ["short", "medium", "long"]

airlines["wait_type"] = pd.cut(airlines["wait_min"], bins=label_ranges, labels=label_names)
print(airlines[["wait_min", "wait_type"]],"\n")

mappings = {"Monday":"weekday", "Tuesday":"weekday", "Wednesday":"weekday", "Thursday":"weekday", "Friday":"weekday",
            "Saturday":"weekend","Sunday":"weekend"}
airlines["day_week"] = airlines["day"].replace(mappings)
print(airlines[["day", "day_week"]])
