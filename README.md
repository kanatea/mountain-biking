# MtB Madeira
*Helping visitors discover Madeira through mountain biking*

## Overview
This project aims to create a tool that catalogues, visualizes, and provides mountain bike trail information in Madeira to bikers by integrating spatial analytics and user insights and feedback within a database.

Group members: Cameron Chalmers & Kana Tateishi

**Key Features**
- Interactive map: Clickable and adjustable map view. 
- Quick and easy overview: Once clicked, a popup offers a quick overview of technical trail information, as well as user ratings and any recently reported issues on a given trail.
- Trails can be filtered by climb category, distance, elevation gain, and star rating.
- Users are able to submit reviews and ratings on trails.
- Users can search for trails based on their location or specific cities within Madeira, with adjustable distance ranges.
- Users are able to report issues or maintenance requests on trails. 
- Users can utilize the search bar to look up trails by name.

## Setup and Execution

**Environment Setup**

1. Install dependencies from `requirements.txt` into your designated environment. 

**Strava API Key Setup and Activation**

2. Run `refresh_access_token.py` in the _`strava_api`_ folder to get the new *access_token* value. 
3. Plug the new access token in the designated place in `test_strava_api.py` in the _`strava_api`_ folder and `load_segments_to_db.py` in the _`etl`_ folder.
4. Run `test_strava_api.py` to make sure you have an active connection to the Strava API.

**Database Setup**

5. Run SQL files 0-4 in the _`db`_ folder in pgAdmin to set up the database, schemas, and tables.
    - `0_create_db.sql` creates the database
    - `1_schema_ext.sql` establishes the schema and adds extensions
    - `2_create_strava_table.sql` and `3_create_table.sql` creates tables and establishes connections
    - `4_data_processing.sql` 

**ETL Process**

6. In the _`etl`_ folder, run `test_db_connection.py` to test the database connection.
7. Run `load_segments_to_db.py` to load Strava trail data into pgAdmin.
8. Run `update_polylines.py` to load trail polyline geometry for our trail data on pgAdmin.

**API Activation**

9. Run `app.py` in the _`api`_ folder to connect the database to the website, which is contained in the _`templates`_ folder as `map.html`. 

**Launch Webpage**

10. Click on the link that appears in your console upon running `app.py` and it should open `map.html`. 


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




