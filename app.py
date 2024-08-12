# Import the dependencies.
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app=Flask(__name__)



#################################################
# Flask Routes

#################################################
@app.route("/")
def welcome ():
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
   )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Find the most recent date in the data set.
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    latest_date = dt.datetime.strptime(latest_date[0], '%Y-%m-%d')
    one_year_ago = latest_date - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_ago).\
    order_by(Measurement.date).all()
    #Always clode the session 
    session.close()
    # Dict with date as key and percepations as the value
    precipitation_date_dic= {date : prcp for date, prcp in precipitation_data}
    
    #return the dic as a json string
    return jsonify(precipitation_date_dic)


    



@app.route("/api/v1.0/stations")
def stations():
    latest_data=session.query(Station.station).all()
    session.close()
    stations = list(np.ravel(latest_data))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
# Get the most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count().desc()).first()[0]

    # Query temperature observations for the most active station for the previous year
    temp_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= prev_year).\
        order_by(Measurement.date).all()
    
    # Close the session
    session.close()
    
    # Convert the results to a list of dictionaries
    tobs_list = [{'date': date, 'tobs': tobs} for date, tobs in temp_data]

    # Return the data as JSON
    return jsonify(tobs_list)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def temp(start=None, end=None):
    # If an end date is provided, query the temperature statistics for the date range
    if end:
        temp_data = session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs)
        ).filter(Measurement.date >= start).\
         filter(Measurement.date <= end).all()
    # If only a start date is provided, query the temperature statistics from the start date
    else:
        temp_data = session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs)
        ).filter(Measurement.date >= start).all()
    
    # Close the session
    session.close()
    
    # Convert the results to a dictionary
    temp_stats = {
        'TMIN': temp_data[0][0],
        'TAVG': temp_data[0][1],
        'TMAX': temp_data[0][2]
    }
    
    # Return the data as JSON
    return jsonify(temp_stats)
if __name__ == '__main__':
    app.run(debug=True)