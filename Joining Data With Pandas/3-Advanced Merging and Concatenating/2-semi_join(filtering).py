# MUTATING JOINS
# Combines data from two tables based on matching observations in both tables

# FILTERING JOINS
# Filter observations from table based on whether or not they match an observation in another table

# SEMI JOIN
# Returns only columns the left table and not the right



# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# video

# genres_tracks = genres.merge(top_tracks, on = "gid")
# top_genres = genres[genres["gid"].isin(genres_track["gid"])]
# print(top_genres)

import pandas as pd
non_mus_tcks = pd.read_csv("non_mus_tcks.csv", index_col=0)
top_invoices = pd.read_csv("top_invoices.csv", index_col=0)
genres = pd.read_csv("genres.csv", index_col=0)

tracks_invoices = non_mus_tcks.merge(top_invoices, on="tid")
top_tracks = non_mus_tcks[non_mus_tcks["tid"].isin(tracks_invoices["tid"])]
cnt_by_gid = top_tracks.groupby("gid", as_index=False).agg({"tid":"count"})
print(cnt_by_gid.merge(genres, on = "gid"))

