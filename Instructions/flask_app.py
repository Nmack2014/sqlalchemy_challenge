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




# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    print("Server received request for 'precipitation' page...")
    
    

    prcp_query = session.query(Measurement.date, Measurement.prcp).all()
    
    prcp_list = []

    for date, prcp in prcp_query:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp_list.append(prcp_dict) 
    
    #prcp_dict = prcp_query.__dict__
    
    session.close()
    return jsonify(prcp_list)

#@app.route("/api/v1.0/stations")
#def stations():
#    print("Server received request for 'precipitation' page...")
#    station_query = session.query(Measurement.station).distinct().all()
#    for results in station_query:
#        station_list.append
    
  



if __name__ == "__main__":
    app.run(debug=True)

