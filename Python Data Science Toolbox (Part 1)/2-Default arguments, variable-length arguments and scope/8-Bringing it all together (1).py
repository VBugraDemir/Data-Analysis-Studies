import pandas as pd

tweets_df = pd.read_csv("tweets.csv")

def count_entries(df, col_name="lang"):
    cols_count = {}
    col=df[col_name]

    for entry in col:
        if entry in cols_count:
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1

    return cols_count

result1 = count_entries(tweets_df)
result2 = count_entries(tweets_df, "source")
print(result1)
print(result2)
