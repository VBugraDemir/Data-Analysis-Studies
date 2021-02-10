from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Chinook.sqlite")
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())