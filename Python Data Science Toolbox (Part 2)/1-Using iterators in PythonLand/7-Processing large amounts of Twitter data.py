# with chunksize an iterable object is created. it creates object till the end of the file.

import pandas as pd

counts_dict = {}

for chunk in pd.read_csv("tweets.csv", chunksize=10):

    for entry in chunk["lang"]:
        if entry in counts_dict:
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
print(counts_dict)
