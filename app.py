import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
base.prepare(engine, reflect=True)

# Save references to each table
measurement1 = base.classes.measurement
station1 = base.classes.station

#################################################
# STATIC DICTIONARIES
#################################################
#example
#justice_league_members = [
#    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
#]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"This is the home page.<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Routes must return HTTP Responses, so we cannot simply 
# return the dictionary
@app.route("/api/v1.0/justice-league-dict")
def justice_league_dict():
    """Return the justice league data as the raw dictionary"""

    return justice_league_members


# Flask comes with a handy jsonify function that creates an 
# HTTP response using the list/dictionary provided
#JSON JSON JSON
@app.route("/api/v1.0/precipitation")
def precipitation_page():
    """Return a list of precipitation data"""

    # Open a communication session with the database
    session = Session(engine)

    # Query all passengers
    results = session.query(measurement1).all()

    # close the session to end the communication with the database
    session.close()

    # Create a dictionary from the row data and append to a list of precip
    precip = []
    for result in results:
        precip_dict = {}
        precip_dict["date"] = measurement1.date
        precip_dict["prcp"] = measurement1.prcp
        precip.append(precip_dict)

    return jsonify(precip)

@app.route("/api/v1.0/stations")
# Return a JSON list of stations from the dataset.
def stations_page():
    """Return a list of all Station names"""

    # Query all stations
    session = Session(engine)
    results = session.query(station1.name).all()

    # close the session to end the communication with the database
    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    print(all_names)
    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.

def tobs_page():
    """Return the stations data as json"""

    return jsonify(stations_listo)



#@app.route("/api/v1.0/<start>")

#@app.route("/api/v1.0/<start>/<end>")


# Index route



if __name__ == '__main__':
    app.run(debug=True)

