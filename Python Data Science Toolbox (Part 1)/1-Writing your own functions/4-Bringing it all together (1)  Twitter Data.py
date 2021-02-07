import pandas as pd
tweets = pd.read_csv("tweets.csv")

lang_counts = {}

col = tweets["lang"]

for entry in col:
    if entry in lang_counts.keys():
        lang_counts[entry] += 1
    else:
        lang_counts[entry] = 1
print(lang_counts)

# doing the same thing by defining a function

def count_entries(df, col_name):
    lang_counts = {}
    col = df[col_name]

    for entry in col:
        if entry in lang_counts:
            lang_counts[entry] += 1
        else:
            lang_counts[entry] = 1
    return lang_counts

result = count_entries(tweets, "lang")
print(result)
