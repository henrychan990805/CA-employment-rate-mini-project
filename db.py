from sqlalchemy import create_engine
import pandas as pd

engine=create_engine('postgresql://postgres:postgres@localhost:5432/database')
conn=engine.connect()

df=pd.read_csv('data/updated_employment_data.csv')
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# creates schema and inserts records
df.to_sql('employment_data', con=conn, if_exists='replace', index=False)
conn.close()