from sqlalchemy import create_engine
import pandas as pd
import os
import pandas as pd

engine=create_engine('postgresql://postgres:postgres@localhost:5432/database')
conn=engine.connect()

df=pd.read_csv('data/updated_employment_data.csv')
df1=pd.read_csv('data/map.csv')


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# creates schema and inserts records
df.to_sql('employment_data', con=conn, if_exists='replace', index=False)
query = "SELECT * FROM employment_data"
df = pd.read_sql(query, conn)
df1.to_sql('map_data', con=conn, if_exists='replace', index=False)
query1 = "SELECT * FROM map_data"
df1 = pd.read_sql(query1, conn)

conn.close()
