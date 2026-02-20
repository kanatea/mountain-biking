DROP TABLE IF EXISTS strava.trails;

CREATE TABLE IF NOT EXISTS strava.trails(    
    id               SERIAL PRIMARY KEY,
    strava_segment_id BIGINT UNIQUE,
    name             varchar(255) NOT NULL,
    region           TEXT DEFAULT 'Madeira',
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
    polyline         TEXT
);




