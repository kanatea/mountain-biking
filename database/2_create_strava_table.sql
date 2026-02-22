--Create table for strava schema - this table will contain all data imported from strava
-- this data will also be accessed from the frontend through our api 

DROP TABLE IF EXISTS strava.trails;

CREATE TABLE IF NOT EXISTS strava.trails(    
    id               SERIAL PRIMARY KEY,
    strava_segment_id BIGINT UNIQUE,
    name             varchar(255) NOT NULL,
    region           TEXT DEFAULT 'Madeira', --all entries should be from the region of madeira 
    distance_m       INTEGER,
    elevation_gain_m INTEGER,
    avg_grade        NUMERIC,
    created_at       TIMESTAMP DEFAULT NOW(),
    start_lat        DOUBLE PRECISION,
    start_lon        DOUBLE PRECISION,
    end_lat          DOUBLE PRECISION,
    end_lon          DOUBLE PRECISION,
    climb_category   INTEGER,
    climb_category_desc TEXT,
    polyline         TEXT                   -- stores the geometry for the trail, otherwise it will be a straight line from the start point to the end point
);





