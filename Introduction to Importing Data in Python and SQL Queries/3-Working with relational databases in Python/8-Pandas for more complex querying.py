import pandas as pd
from sqlalchemy import create_engine

# pd.set_option("display.max_columns", None)
engine = create_engine("sqlite:///Chinook.sqlite")

df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeID >= 6 ORDER BY BirthDate", engine)
print(df.head())
