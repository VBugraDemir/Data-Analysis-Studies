import recordlinkage
import pandas  as pd

restaurants = pd.read_csv("restaurants_L2.csv", index_col=0)
restaurants_new = pd.read_csv("restaurants_L2_dirty.csv", index_col=0)

indexer = recordlinkage.Index()
indexer.block("type")
pairs = indexer.index(restaurants, restaurants_new)
print(pairs)

# comparison object

comp_cl = recordlinkage.Compare()
comp_cl.exact("city", "city", label="city")
comp_cl.exact("type", "type", label="cuisine_type")
comp_cl.string("name", "name", label="name", threshold = 0.8)
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

matches = potential_matches[potential_matches.sum(axis=1) >= 3]
print(matches)

matching_indices = matches.index.get_level_values(level = 1)
print(matching_indices)
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]
print(non_dup)
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
