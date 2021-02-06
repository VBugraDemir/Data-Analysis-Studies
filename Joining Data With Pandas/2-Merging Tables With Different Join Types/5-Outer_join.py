# Merge begins_actors to returns_actors on id with outer join using suffixes
# begins_returns = begins_actors.merge(returns_actors,
#                                      on = "id",
#                                      how = "outer",
#                                      suffixes=["_beg", "_ret"])

# Create an index that returns true if name_beg or name_ret are null
# m = ((begins_returns['name_beg'].isnull()) |
#      (begins_returns['name_ret'].isnull()))

# Print the first few rows of begins_returns
# print(begins_returns[m].head())

# the batman data is not found so these codes cant be run.
# the thing is it is a outer joining and there are lots of NaN data
# with operator only those rows are selected where the actor played in
# only one of the two movies.

# so outer join can be used to find a value that can be only found in one table
# and that is not shared within tables...
