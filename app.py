from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text, inspect
import psycopg2

app = Flask(__name__)
DB_NAME = 'database'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

def get_data_from_database(dataset):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {dataset}')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/state_data')
def data():
    data = get_data_from_database('state_data')
    return data

@app.route('/county_data')
def county_data():
    data = get_data_from_database('county_data')
    return data

@app.route('/metropolitan_data')
def county_data():
    data = get_data_from_database('metropolitan_data')
    return data

@app.route('/data')
def data():
    data = get_data_from_database('employment_data')
    return data

if __name__ == '__main__':
    app.run(debug=True)