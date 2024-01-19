#!/usr/bin/python3

import config
import pandas as pd
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask import Flask, render_template
from flask_cors import CORS

#database setup
database = 'meteorite'

engine = sqlalchemy.create_engine(f'postgresql://{config.username}:{config.password}@localhost:5432/{database}')
Base = automap_base()
Base.prepare(autoload_with=engine)
meteorites = Base.classes.meteorites
connection = engine.connect()

query = sqlalchemy.text("SELECT * FROM meteorites")
data = engine.execute(query)

meteorites_df = pd.read_sql_query('select * from "meteorites"',con=engine)

mass_df = meteorites_df.loc[:, ["name","class", "mass"]]


#finding average of mass per type
avg_mass = mass_df.groupby("class")
avg_mass_df = avg_mass["mass"].mean()
print(avg_mass_df)

#for record in data:
    #print(record)

#flask setup
    
app = Flask(__name__)
CORS(app)

#flask routes

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/mass-graph<br/>"
        f"/api/v1.0/yearly-graph<br/>"
        f"/api/v1.0/landings-map"
    )

@app.route("/api/v1.0/mass-graph")
def mass_graph():
    class_mean_mass = mass_df.groupby('class')['mass'].mean().reset_index()
    top_50_classes = class_mean_mass.nlargest(50, 'mass')
    top_50_dict = top_50_classes.to_dict('list')
    
    return jsonify(top_50_dict)

@app.route("/api/v1.0/yearly-graph")
def year_graph():
    year_count = meteorites_df.groupby("year")
    year_count = year_count["name"].count()
    year_count = year_count.sort_index()
    year_count_dict = year_count.to_dict()
    
    return jsonify(year_count_dict)

@app.route("/api/v1.0/landings-map")
def landings_map():
    
    return()

#runs the flask api in browser
if __name__ == '__main__':
    app.run(debug=True)