import pandas as pd

tracks_master_list = {
    "tid": [1853, 1854, 1857],
    "name": ["Battery", "Master of Puppets", "Disposable Heroes"],
    "aid": [152, 152, 152],
    "mtid": [1, 1, 1],
    "gid": [3, 3, 3],
    "composer": ["J.Hetfield/L.Ulrich", "K.Hammett", "J.Hetfield/L.Ulrich"],
    "u_price": [0.99, 0.99, 0.99]
}
i = [0, 1, 4]
tracks_master = pd.DataFrame(tracks_master_list, index=i)

tracks_ride_list = {
    "tid": [1874, 1875, 1876, 1877, 1878],
    "name": ["Fight Fire With Fire", "Ride The Lightning", "For Whom The Bell Tolls", "Fade To Black", "Trapped Under Ice"],
    "aid": [154, 154, 154, 154, 154],
    "mtid": [1, 1, 1, 1, 1],
    "gid": [3, 3, 3, 3, 3],
    "u_price": [0.99, 0.99, 0.99, 0.99, 0.99]
}
tracks_ride = pd.DataFrame(tracks_ride_list)

tracks_st_list = {
    "tid": [1882, 1883, 1884, 1885, 1886],
    "name": ["Frantic", "St. Anger", "Some Kind Of Monster", "Dirty Window", "Invisible Kid"],
    "aid": [155, 155, 155, 155, 155],
    "mtid": [1, 1, 1, 1, 1],
    "gid": [3, 3, 3, 3, 3],
    "u_price": [0.99, 0.99, 0.99, 0.99, 0.99]
}
tracks_st = pd.DataFrame(tracks_st_list)


# Concatenate the tracks
# sort is sorting the columns
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], sort=True)
print(tracks_from_albums)
print()

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], sort=True, ignore_index=True)
print(tracks_from_albums)
print()

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], join="inner", sort=True, ignore_index=True)
print(tracks_from_albums)
