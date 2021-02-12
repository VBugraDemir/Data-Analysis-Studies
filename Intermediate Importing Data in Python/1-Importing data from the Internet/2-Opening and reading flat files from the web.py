import pandas as pd
# from urllib.request import urlretrieve
import matplotlib.pyplot as plt
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
df = pd.read_csv(url, sep = ";")
print(df.head())

pd.DataFrame.hist(df.iloc[:,0:1])   # df.iloc[:,[0]] or df[["fixed acidity"]]
plt.xlabel("fixed acidity (g(tartaric acid)/dm$^3$)")
plt.ylabel("count")
plt.show()
