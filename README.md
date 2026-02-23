# MtB Madeira
*Helping visitors discover Madeira through mountain biking*

## Overview
This project aims to create a tool that catalogues, visualizes, and provides mountain bike trail information in Madeira to bikers by integrating spatial analytics and user insights and feedback within a database.

**Group members:** Cameron Chalmers & Kana Tateishi (●＾o＾●)

### Key Features (◕‿◕✿)
- **Interactive map:** Clickable and adjustable map view. 
- **Quick and easy overview:** Once clicked, a popup offers a quick overview of technical trail information, as well as user ratings and any recently reported issues on a given trail.
- **Filter trails:** Filter by climb category, distance, elevation gain, and star rating.
- **Submit ratings and reviews:** Users are able to submit reviews and ratings on trails.
- **Search trails based on location:** Users can search for trails based on their location or specific cities within Madeira, with adjustable distance ranges.
- **Report issues:** Users are able to report issues or submit maintenance requests on trails. 
- **Search trails based on name:** Users can utilize the search bar to look up trails by name.

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
pgAdmin are used for spatial data storage and analysis.

**Tables**
- `strava.trails`: Stores trail information (trail name, distance, elevation gain, trail grade, start and end point, climb category, polylines/trail geometry)
- `pa.users`: Stores usernames for tracking feedback
- `pa.trails`: Stores trail names for ID'ing reviews and maintenance issues
- `pa.trail_ratings`: Collects feedback on trails (ratings, text reviews, timestamp)
- `pa.maintenance`: Collects feedback on trail condition and any issues (requests, timestamp)


## ETL (Extract, Transform, Load)

### Extract
- **Strava:** Provides mountain biking trail data with attributes that include name of trail, overall distance, trail grade, elevation gain, climb category, trail geometry, and the start and end point of the trail. Data extraction uses the Strava API. 
- **OSM:** Providing the basemap for search context on the frontend site, Leaflet was used to facilitate the OSM to website connection.

### Transform
- Trails were filtered based on location, the island of Madeira were split into 9 tiles, drawn by specified coordinates, and trails located within each tile were called.
- Once loaded into the database, the climb categories were recoded for clarification.

### Load
- Processed data is loaded into pgAdmin in the `strava.trails` table, which is displayed as trial data on the frontend
- The frontend site allows users to submit reviews and maintenance requests, which updates the pgAdmin database. The review data is stored on `pa.trail_ratings` and the maintenance data is stored on `pa.maintenance`.
- Average trail rating data and most recent maintenance requests are called from the database back to the frontend to dynamically display user input.

## API
- `GET /trails`: Retrieve running trail information
- `POST /reviews`: Submit ratings and reviews on specified trails
- `POST /report`: Submit a maintenance report or issue on specified trails
- `GET /trail_ratings`: Retrieve average trail rating submitted by users
- `GET /maintenance`: Retrieve most recent maintenance request submitted by users

## Libraries and Packages
- python
    - time, os, requests
- psycopg2-binary, psycopg2
    - psycopg2 
- flask
    - flask, jsonify, render_template, request


















