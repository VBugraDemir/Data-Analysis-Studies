import json

tweets_data_path = "tweets2.txt"
tweet_file = open(tweets_data_path, "r")
tweets_data = []

for line in tweet_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

print(tweets_data[0].keys())
