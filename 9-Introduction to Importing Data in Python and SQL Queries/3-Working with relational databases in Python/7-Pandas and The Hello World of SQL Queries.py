import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Chinook.sqlite")
df = pd.read_sql_query("SELECT * FROM Album", engine)
print(df.head())

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()
print(df1.head())