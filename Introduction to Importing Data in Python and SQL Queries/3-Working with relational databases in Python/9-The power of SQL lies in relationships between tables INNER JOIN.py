import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Chinook.sqlite")

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Artist")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())

with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())
