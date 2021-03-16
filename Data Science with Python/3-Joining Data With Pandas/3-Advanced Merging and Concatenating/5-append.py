# The .concat() method is excellent when you need a lot of control over how concatenation is performed.
# However, if you do not need as much control, then the .append() method is another option.
import pandas as pd
invoice_items = pd.read_csv("invoice_items.csv", index_col= 0)

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

metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort = False)
tracks_invoices = metallica_tracks.merge(invoice_items, on = "tid")
tracks_sold = tracks_invoices.groupby(["tid", "name"]).agg({"quantity":"sum"})
print(tracks_sold.sort_values("quantity", ascending= False))