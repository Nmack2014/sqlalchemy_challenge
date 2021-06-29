# 1. import Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite").connect()

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station


session = Session(engine)

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'home' page...")
    return (f"<h2>Climate App HomePage</h2><br/>"
    f"<ul><li>Precipitation Page - <code>/api/v1.0/precipitation</code></li></ul>"
    f"<ul><li>Stations Page- <code>/api/v1.0/stations</code></li></ul>"
    f"<ul><li>Temperature Observations Page- <code>/api/v1.0/tobs</code></li></ul>"
    )


# 4. Define what to do when a user hits the /about route

@app.route("/api/v1.0/precipitation")
def precipitation():
    
   
    print("Server received request for 'precipitation' page...")
    

    prcp_query = session.query(Measurement.date, Measurement.prcp).all()  
    prcp_dict = prcp_query.__dict__
    
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'precipitation' page...")
    
    station_query = session.query(Measurement.station).distinct().all()
    station_dict = station_query.__dict__
    
    return jsonify(station_dict)




session.close()

if __name__ == "__main__":
    app.run(debug=True)

