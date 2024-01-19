#!/usr/bin/python3

import config
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

#database setup
database = 'meteorite'

engine = sqlalchemy.create_engine(f'postgresql://{config.username}:{config.password}@localhost:5432/{database}')
Base = automap_base()
Base.prepare(autoload_with=engine)
meteorites = Base.classes.meteorites
connection = engine.connect()

query = sqlalchemy.text("SELECT * FROM meteorites")
data = engine.execute(query)


#for record in data:
    #print(record)

#flask setup
    
app = Flask(__name__)

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
    
    
    return ()

@app.route("/api/v1.0/yearly-graph")
def year_graph():

    return()

@app.route("/api/v1.0/landings-map")
def landings_map():

    return()

#runs the flask api in browser
if __name__ == '__main__':
    app.run(debug=True)