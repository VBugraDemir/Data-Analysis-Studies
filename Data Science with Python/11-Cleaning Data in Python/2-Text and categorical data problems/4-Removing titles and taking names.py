import pandas as pd

airlines = pd.read_csv("airlines_final_names199.csv", index_col=0)
# 199 tanesini ayrı csv ye yazmak yerine chunksize kullanmalıydın. diğerinde var.
names = pd.read_csv("names.csv", index_col=0)
airlines = airlines.join(names)

airlines["full_name"] = airlines["full_name"].str.replace("Dr. ", "")
airlines["full_name"] = airlines["full_name"].str.replace("Mr. ", "")
airlines["full_name"] = airlines["full_name"].str.replace("Miss ", "")
airlines["full_name"] = airlines["full_name"].str.replace("Ms. ", "")
assert airlines["full_name"].str.contains("Ms.|Mr.|Miss|Dr.").any() == False
print(airlines)
