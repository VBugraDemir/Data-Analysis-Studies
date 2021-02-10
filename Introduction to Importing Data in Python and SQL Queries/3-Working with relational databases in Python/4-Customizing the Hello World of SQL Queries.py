# Open engine in context manager
# Perform query and save results to DataFrame: df

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Chinook.sqlite")
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
print(len(df))
print(df)