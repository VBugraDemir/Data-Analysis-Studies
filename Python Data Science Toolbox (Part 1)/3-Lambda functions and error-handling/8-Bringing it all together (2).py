import pandas as pd

tweets_df = pd.read_csv("tweets.csv")

def count_entries(df, col_name = "lang"):
    cols_count = {}
    try:
        col = df[col_name]
        for entry in col:
            if entry in cols_count:
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        return cols_count
    except:
        print("The DataFrame does not have a"  + col_name + " column.")

result1 = count_entries(tweets_df, 'lang')
print(result1)