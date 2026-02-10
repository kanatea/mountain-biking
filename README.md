# MtB Madeira
*Helping visitors discover Madeira through mountain biking*

## Overview
This project aims to create a tool that catalogues, visualizes, and provides mountain bike trail information in Madeira to bikers by integrating spatial analytics and user insights and feedback within a database.

Group members: Cameron Chalmers & Kana Tateishi

## Setup and Execution
**Database Setup**
**Environment Setup**
**ETL Process**
**API Key Setup** Open _`key.py`_ with the API key.
**API Activation**

## Database
PostgreSQL and PostGIS are used for spatial data storage and analysis.

**Tables**
trail - Stores trail information (INSERT ATTRIBUTES)
user - User information for tracking feedback
ratings - User feedback on trails

## ETL (Extract, Transform, Load)

### Extract
Data sources:
- Strava - Provides mountain biking trail data with attributes that include name of trail, overall distance, the average grade, elevation gain, and the start and end point of the trail. 
- OSM - Basemap

### Transform
Data processing:
- All data is standardized to 
- Shapefile consolidating all data

### Load
Database integration:
- Processed data is loaded into PostgreSQL/PostGIS in the trail table.
- The rating table stores rider ratings and feedback.

## API


