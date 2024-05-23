from sqlalchemy import create_engine
import pandas as pd

engine=create_engine('postgresql://postgres:postgres@localhost:5432/database')
conn=engine.connect()

df=pd.read_csv('data/updated_employment_data.csv')
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# creates schema and inserts records
df.to_sql('employment_data', con=conn, if_exists='replace', index=False)
county_df = pd.read_csv('data/county_employment_data.csv')
metro_df = pd.read_csv('data/metropolitan_area_data.csv')
state_df = pd.read_csv('data/state_employment_data.csv')
county_df.to_sql('county_data', con=conn, if_exists='replace', index=False)
metro_df.to_sql('metropolitan_data', con=conn, if_exists='replace', index=False)
state_df.to_sql('state_data', con=conn, if_exists='replace', index=False)
conn.close()