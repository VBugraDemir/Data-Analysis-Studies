import pandas as pd

tweets = pd.read_csv("tweets.csv")

tweet_time = tweets["created_at"]

tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == "19"]
print(tweet_clock_time)
