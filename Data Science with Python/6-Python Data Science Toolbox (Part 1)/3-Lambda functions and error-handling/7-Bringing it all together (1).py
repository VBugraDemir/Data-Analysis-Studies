import pandas as pd

tweets_df = pd.read_csv("tweets.csv")

result = filter(lambda x: x.startswith("RT"), tweets_df["text"])
result_list = list(result)

for tweet in result_list:
    print(tweet)

