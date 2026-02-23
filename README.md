# MtB Madeira 🏍ﮩ٨ـﮩﮩ٨ـ
✧･ﾟ: *✧･ﾟ:* *Helping visitors discover Madeira through mountain biking* *:･ﾟ✧*:･ﾟ✧ 

## Overview (｡•̀ᴗ-)✧
This project aims to create a tool that catalogues, visualizes, and provides mountain bike trail information in Madeira to bikers by integrating spatial analytics and user insights and feedback within a database.

**Group members:** Cameron Chalmers & Kana Tateishi (￣▽￣)ノ⟡ 

### Key Features (◕‿◕✿)
- **Interactive map:** Clickable and adjustable map view. 
- **Quick and easy overview:** Once clicked, a popup offers a quick overview of technical trail information, as well as user ratings and any recently reported issues on a given trail.
- **Filter trails:** Filter by climb category, distance, elevation gain, and star rating.
- **Submit ratings and reviews:** Users are able to submit reviews and ratings ★ on trails.
- **Search trails based on location:** Users can search for trails based on their location or specific cities within Madeira, with adjustable distance ranges.
- **Report issues:** Users are able to report issues or submit maintenance requests on trails. 
- **Search trails based on name:** Users can utilize the search bar to look up trails by name.

## Setup and Execution

**Environment Setup** 

1. Install dependencies from `requirements.txt` into your designated environment.
2. Import package dependencies from `imports.py` into your designated environment.

**Strava API Key Setup and Activation**

A registered Strava account is required to set up an app and access the Strava API. 

3. Access the Strava website and follow these directions to set up your app: https://developers.strava.com/. You may proceed to the following bulleted steps once your app is set up on the Strava website.

    - Run `generate_auth_url.py` in the _`archive`_ folder to receive an *authorization/authentication code*.
    - Plug the *authorization/authentication code* in the designated place in `exchange_code_for_token.py` in the _`archive folder`_ to get the *access_token* value.
    - Plug the *access_token* value in the designated place in `refresh_access_token.py` in the _`strava_api`_ folder.
  
    Step 3 needs to only be done once; once the Strava API is activated, only steps 4 onward are required to initialize the connection every time.

4. Run `refresh_access_token.py` in the _`strava_api`_ folder  to get the new *access_token* value. 
5. Plug the new *access token* in the designated place in `test_strava_api.py` in the _`strava_api`_ folder and `load_segments_to_db.py` in the _`etl`_ folder.

    _(Optional)_ Run `test_strava_api.py` to make sure you have an active connection to the Strava API.

**Database Setup**

6. Run SQL files 0-3 in the _`database`_ folder in pgAdmin to set up the database, schemas, and tables.
    - `0_create_db.sql` creates the database
    - `1_schema_ext.sql` establishes the schema and adds extensions
    - `2_create_strava_table.sql` and `3_create_table.sql` creates tables and establishes connections

    _(Optional)_ In the _`etl`_ folder, run `test_db_connection.py` to test the database connection.

**ETL Process**

7. In the _`etl`_ folder, run `load_segments_to_db.py` to load Strava trail data into pgAdmin.
8. Run `update_polylines.py` to load trail polyline geometry for our trail data on pgAdmin.
9. Run `4_data_processing.sql` from  the _`database`_ folder in pgAdmin for data transformation and processing.

    _(Optional)_ Run `sample_data.sql` from  the _`database`_ folder in pgAdmin to pre-populate sample review data for the website.

**API Activation**

10. Run `app.py` in the _`api`_ folder to connect the database to the website, which is contained in the _`templates`_ folder as `map.html`. 

**Launch Webpage**

11. Click on the link that appears in your console upon running `app.py` and it should open `map.html`. The website is ready to go! ٩(ˊᗜˋ*)و ♡


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
- Trails were filtered based on location, the island of Madeira were split into 9 tiles, drawn by specified coordinates, and trails located within each tile were called from the Strava API.
- Once loaded into the database, the climb categories were recoded for clarification, which is used for their color coding on the frontend.
- Climb distance and elevation gain were similarly grouped into buckets for filtering functionality on the frontend.

### Load
- Processed data is loaded into pgAdmin in the `strava.trails` table, which is displayed as trial data on the frontend
- The frontend site allows users to submit reviews and maintenance requests, which updates the pgAdmin database. The review data is stored on `pa.trail_ratings` and the maintenance data is stored on `pa.maintenance`.
- Average trail rating data and most recent maintenance requests are called from the database back to the frontend to dynamically display user input.

## API
- `GET /trails`: Retrieve running trail information
- `POST /reviews`: Submit ratings and reviews on specified trails
- `POST /report`: Submit a maintenance report or issue on specified trails
- `GET /trail_ratings`: Retrieve average trail rating submitted by users
- `GET /latest_report`: Retrieve most recent maintenance request submitted by users (within the last two weeks)

## Libraries and Packages
- python
    - time, os, requests
- psycopg2-binary, psycopg2
    - psycopg2 
- flask
    - flask, jsonify, render_template, request

## Reflection and Future Work
- The number of tiles that enclose our project area of Madeira could be greater, or each tile can be smaller, to increase the number of trails that can be called from Strava, as each Strava API inquiry per tile yields a maximum of 10 trails. 
- Additional sources can be identified to make data on existing trails more robust, as well as increase the number and diversity of trails included within the map.
- Additional features on the frontend, such as being able to view all reviews or all submitted reports, would create a more robust user experience.
- Creating a feedback mechanism of confirming the existence and status of reported issues, such as a fallen tree on a trail (like in Waze), would add more database connections and also enable a more interactive user experience.

 ##
_Thanks for reading! (=^･ω･^=)_



