# Verifying integrity of the data
# checking the relationships (one_to_one or one_to_many)
# one_to_one or one_to_many or many_to_many or one_to_one
# if the relationship is not as expected then an error is raised
import pandas as pd
tracks_list = {
    "tid":[2, 3, 4],
    "name":["Balls to the wall", "Fast As a Shark", "Restless and Wild"],
    "aid":[2, 3, 3],
    "mtid":[2, 2, 2],
    "gid":[1, 1, 1],
    "u_price":[0.99, 0.99, 0.99]
}
tracks = pd.DataFrame(tracks_list)

specs_list = {
    "tid":[2, 3, 2],
    "milliseconds":[342562, 230619, 252051],
    "bytes":[5510424, 3990994, 4331779]
}
specs = pd.DataFrame(specs_list)
# tracks.merge(specs, on = "tid", validate= "one_to_one") # error is raised
print(tracks.merge(specs, on = "tid", validate= "one_to_many")) # no error