import json
import pandas as pd

tweets_data_path = "tweets2.txt"
tweet_file = open(tweets_data_path, "r")
tweets_data = []
for line in tweet_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

df = pd.DataFrame(tweets_data, columns=["text", "lang"])

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False


[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

for index, row in df.iterrows():
    clinton += word_in_text("clinton", row["text"])
    trump += word_in_text("trump", row["text"])
    sanders += word_in_text("sanders", row["text"])
    cruz += word_in_text("cruz", row["text"])

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes = True)

cd = ["clinton", "trump", "sanders", "cruz"]
print( [clinton, trump, sanders, cruz])
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel = "count")
# sns.barplot(cd, [clinton, trump, sanders, cruz])
# plt.ylabel("count")
plt.show()
