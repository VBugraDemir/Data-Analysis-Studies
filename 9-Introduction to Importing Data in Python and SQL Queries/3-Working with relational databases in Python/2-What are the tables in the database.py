from sqlalchemy import create_engine
engine = create_engine("sqlite:///Chinook.sqlite")
table_names = engine.table_names()
print(table_names)