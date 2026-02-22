# MtB Madeira
*Helping visitors discover Madeira through mountain biking*

## Overview
This project aims to create a tool that catalogues, visualizes, and provides mountain bike trail information in Madeira to bikers by integrating spatial analytics and user insights and feedback within a database.

Group members: Cameron Chalmers & Kana Tateishi

## Setup and Execution
**Strava API Key Setup and Activation**

1. Read requirements.txt file into your Python environment. 
2. Run the refresh_access_token script in the strava_api folder on VScode to get the new access_token value. 
3. Plug the new access token value in the designated place in the test_strava_api script in the strava_api folder and load_segments_to_db in the etl folder.
4. Run test_strava_api on VScode to make sure you have an active connection to the Strava API.

**Database Setup**

5. Run SQL files 0-4 in the db folder in pg admin to set up the database, schemas, and tables.

**ETL Process**

6. Run the test_db_connection script in VScode to test the database connection.
7. Run load_segments_to_db on VScode to load Strava trail data into pg admin.
8. Run update_polylines to load trail polyline geometry for our trail data on pg admin.

**API Activation**

9. Run app.py on VScode to connect the database to the website, which is contained in the templates folder as map.html. 
10. Click on the link that appears in your console upon running app.py and it should open the html file. 

**Environment Setup**

## Database
PostgreSQL and PostGIS are used for spatial data storage and analysis.

**Tables**
trail - Stores trail information (INSERT ATTRIBUTES)
ratings - User feedback on trails

## ETL (Extract, Transform, Load)

### Extract
Data sources:
- Strava - Provides mountain biking trail data with attributes that include name of trail, overall distance, the average grade, elevation gain, and the start and end point of the trail. 
- OSM - Basemap

### Transform
Data processing:
- All data is standardized to EPSG:2942 (Madeira 1936 / UTM zone 28N)
- Shapefile consolidating basemap with Strava data 

### Load
Database integration:
- Processed data is loaded into PostgreSQL/PostGIS in the trail table.
- The rating table stores rider ratings and feedback.

## API



