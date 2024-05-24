import sqlalchemy
import plotly.graph_objs as go
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text, inspect,MetaData
import pandas as pd
import hvplot.pandas

from sqlalchemy.orm import Session


#engine=create_engine('sqlite:///database.db', echo=True)
engine=create_engine('postgresql://postgres:postgres@localhost:5432/database')
# reflect an existing database into a new model
metadata = MetaData()
metadata.reflect(bind=engine)
# Save references to each table
employment_data_table = metadata.tables['employment_data']
map=metadata.tables['map_data']
# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app=Flask(__name__)


@app.route("/")
def home():
    # https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates
    return render_template('index.html')

@app.route('/data')
def get_data(): 
    results = session.query(employment_data_table).all()
    session.close()
    results=[tuple(row[1:]) for row in results]
    caldata=[each_item for each_item in results if each_item[1]=='California']
    return caldata

@app.route('/job')
def get_pie():
    results = session.query(employment_data_table).all()
    session.close()
    results=[tuple(row[1:]) for row in results]
    caldata=[each_item for each_item in results if each_item[1]=='California']
    yeardata=[each_item for each_item in caldata if each_item[2]==2020]
    inddata=[each_item for each_item in caldata if each_item[5]=='Chemical & Allied Products Merchant whol']

    return inddata


    


    

if __name__ == '__main__':
    app.run(debug=True)