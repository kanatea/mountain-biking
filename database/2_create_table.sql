DROP TABLE IF EXISTS strava.trails;

CREATE TABLE IF NOT EXISTS strava.trails
(    id               SERIAL PRIMARY KEY,
    strava_segment_id BIGINT UNIQUE,
    name             TEXT NOT NULL,
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


DROP TABLE IF EXISTS pa.users;

CREATE TABLE IF NOT EXISTS pa.users (
	id               SERIAL,
    user_id 		 BIGINT UNIQUE,
    username         varchar(255) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS pa.trails;

CREATE TABLE IF NOT EXISTS pa.trails(
	id               SERIAL,
    trail_id 		 BIGINT UNIQUE NOT NULL PRIMARY KEY,
    trail_name       TEXT
);

DROP TABLE IF EXISTS pa.trail_ratings;

CREATE TABLE IF NOT EXISTS pa.trail_ratings (
	id         SERIAL PRIMARY KEY,
    trail_id   INTEGER NOT NULL REFERENCES pa.trails(trail_id),
	rating      INTEGER CHECK (rating BETWEEN 1 AND 5),
	username    varchar(255) NOT NULL REFERENCES pa.users(username),
    comment     TEXT,
	created_at TIMESTAMP DEFAULT NOW()
);


DROP TABLE IF EXISTS pa.maintenance;

CREATE TABLE IF NOT EXISTS pa.maintenance (
	id               SERIAL PRIMARY KEY,
    feedback_id 	 BIGINT UNIQUE,
    trail_id        INTEGER NOT NULL REFERENCES pa.trails(trail_id),
	maint_comment	 TEXT,
	lat			  	 TEXT,
	long			 TEXT
);


