# creating dataframe by using list of dicts.
# tweet_data is a list that contains dicts
# dataframes can be created from list of dicts or dicts of lists (look 4-4)
import json
import pandas as pd

tweets_data_path = "tweets2.txt"
tweet_file = open(tweets_data_path, "r")
tweets_data = []
for line in tweet_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

df = pd.DataFrame(tweets_data, columns=["text", "lang"])
print(df.head())

