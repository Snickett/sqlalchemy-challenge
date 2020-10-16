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
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurement1 = base.classes.measurement
station1 = base.classes.station

#################################################
# STATIC DICTIONARIES
#################################################
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},

]

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
    """Return the precipitation data as json"""

    return jsonify(precipitation_listo)

@app.route("/api/v1.0/stations")
def stations_page():
    """Return the stations data as json"""

    return jsonify(stations_listo)

@app.route("/api/v1.0/stations")
def stations_page():
    """Return the stations data as json"""

    return jsonify(stations_listo)


# Index route



if __name__ == "__main__":
    app.run(debug=True)
