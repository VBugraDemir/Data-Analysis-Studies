import pandas as pd

tweets_df = pd.read_csv("tweets.csv")

def count_entries(df, *args):
    cols_count = {}

    for col_name in args:
        col = df[col_name]

        for entry in col:
            if entry in cols_count:
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return cols_count

result1 = count_entries(tweets_df, "lang")
result2 = count_entries(tweets_df, "lang", "source")
print(result1)
print(result2)