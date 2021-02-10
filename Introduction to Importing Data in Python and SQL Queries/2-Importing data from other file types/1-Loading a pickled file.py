# the dictionary is pickled before

import pickle

with open("data.pkl", "rb") as file:
    d = pickle.load(file)

print(d)
print(type(d))
