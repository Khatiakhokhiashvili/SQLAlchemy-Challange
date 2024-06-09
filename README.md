# SQLAlchemy-Challange
# Climate Analysis and Exploration

## Overview

This project involves performing a basic climate analysis and data exploration of climate data from Hawaii. Using Python, SQLAlchemy, Pandas, and Matplotlib, various climate-related queries and visualizations were performed to gain insights into the dataset.

## Data Sources

- `hawaii.sqlite`: SQLite database containing climate data.
- `hawaii_measurements.csv`: CSV file with climate measurements.
- `hawaii_stations.csv`: CSV file with station information.

## Tools and Libraries

- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Jupyter Notebook

## Project Structure

- `climate_starter.ipynb`: Jupyter notebook containing the code for data analysis and exploration.
- `hawaii.sqlite`: SQLite database file.
- `hawaii_measurements.csv`: CSV file with climate measurements.
- `hawaii_stations.csv`: CSV file with station information.

## Analysis Steps

1. **Database Setup and Connection**
   - Used SQLAlchemy's `create_engine` function to connect to the SQLite database.
   - Reflected the database tables into classes using `automap_base`.
   - Linked Python to the database by creating a SQLAlchemy session.

2. **Climate Analysis**
   - Queried the total number of stations in the dataset.
   - Identified the most-active stations by observation counts.
   - Calculated the lowest, highest, and average temperatures for the most-active station.
   - Retrieved the last 12 months of precipitation data and plotted the results.
   - Calculated summary statistics for precipitation data.

3. **Station Analysis**
   - Queried the total number of stations.
   - Listed stations and observation counts in descending order.
   - Identified the station with the greatest number of observations.
   - Queried the last 12 months of temperature observation data for the most-active station and plotted the results as a histogram.

