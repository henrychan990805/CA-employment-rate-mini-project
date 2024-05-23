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

@app.route('/map')
def get_map():
    # mapplot=session.query(map).all()
    # session.close()
    # mapresult=[tuple(row[1:]) for row in mapplot]
    # return mapresult
    map_df=pd.read_csv('data/map.csv')
    map_plot = map_df.hvplot.points(
        "Longitude",
        "Latitude",
        geo=True,
        tiles="OSM",
        frame_width=1000,
        frame_height=1000,
        size="Regional Unemployment",
        scale=0.03,
        color="Area Name",
        hover_cols=['Area Name', 'Regional Unemployment'],
        title="Average unemployment by area"
    )

    plot_html = hvplot.render(map_plot, backend='bokeh')

    return render_template('map_template.html', plot_html=plot_html)



    

if __name__ == '__main__':
    app.run(debug=True)