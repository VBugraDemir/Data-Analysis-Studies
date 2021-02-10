from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Chinook.sqlite")
print(engine.table_names())
con = engine.connect()
rs = con.execute("SELECT * FROM Album")
df = pd.DataFrame(rs.fetchall())
con.close()
# df.columns = rs.keys()
print(df)

