# MtB Madeira
*Helping visitors discover Madeira through mountain biking*

## Overview
This project aims to create a tool that catalogues, visualizes, and provides mountain bike trail information in Madeira to bikers by integrating spatial analytics and user insights and feedback within a database.

Group members: Cameron Chalmers & Kana Tateishi

## Setup and Execution
**Strava API Key Setup and Activation**
Run the refresh_access_token script in the strava_api folder to get the new access_token value. 
Plug the new access token value in the designated place in the test_strava_api script in the strava_api folder and load_segments_to_db in the etl folder.
Run test_strava_api to make sure you have an active connection to the Strava API.
**Database Setup**
**ETL Process**
**API Activation**
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



