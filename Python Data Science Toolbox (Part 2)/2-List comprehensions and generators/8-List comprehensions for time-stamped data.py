import pandas as  pd

df = pd.read_csv("tweets.csv")

tweet_time = df["created_at"]

tweet_clock_time = [entry[11:19] for entry in tweet_time]
print(tweet_clock_time)
