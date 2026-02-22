-- Creating schemas and adding extensions

-- Not sure why we called it pa, but this schema will contain front-end user-specific interactions
CREATE SCHEMA IF NOT EXISTS pa
  AUTHORIZATION postgres;

-- This schema will contain data imported from the strava api
CREATE SCHEMA IF NOT EXISTS strava
  AUTHORIZATION postgres;

-- PostGIS Extensions
CREATE EXTENSION postgis;
CREATE EXTENSION pgrouting;




