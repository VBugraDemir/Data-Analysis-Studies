import pandas as pd
# a = pd.read_csv("tweets.csv", chunksize=10)
# b  = next(a)
# print(b)
def count_entries(csv_file, c_size, colname):
    counts_dict = {}

    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[colname]:
            if entry in counts_dict:
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict

result_counts = count_entries("tweets.csv", 10, "lang")
print(result_counts)
