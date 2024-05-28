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
html_chart_df = pd.read_csv('data/html_chart.csv')
employment_summary_df = pd.read_csv('data/employment_summary_df.csv')
CA_Counties_df = pd.read_csv('data/CA_Counties')
county_df.to_sql('county_data', con=conn, if_exists='replace', index=False)
metro_df.to_sql('metropolitan_data', con=conn, if_exists='replace', index=False)
state_df.to_sql('state_data', con=conn, if_exists='replace', index=False)
html_chart_df.to_sql('bar_charts', con = conn, if_exists='replace',index=False)
employment_summary_df.to_sql('employment_summary',con = conn, if_exists='replace',index = False)

conn.close()