# Importing the dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Accessing up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflecting the database
Base = automap_base()
Base.prepare(engine, reflect=True)

# Assigning the variables to the database
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Setting up Flask
app = Flask(__name__)

# Defining the main route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!!\n
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end
    ''')

# Defining the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

if __name__ == "__main__":
    app.run(debug=True)