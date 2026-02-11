CREATE TABLE IF NOT EXISTS public.trails (
	id               SERIAL PRIMARY KEY,
    strava_segment_id BIGINT UNIQUE,
    name             TEXT NOT NULL,
    distance_m       INTEGER,
    elevation_gain_m INTEGER,
    average_grade    NUMERIC,
    start_point      TEXT,
    end_point        TEXT
);


CREATE TABLE IF NOT EXISTS public.trail_ratings (
	id SERIAL PRIMARY KEY,
	trail_id INTEGER REFERENCES trails(id) ON DELETE CASCADE,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.users (
	id               SERIAL PRIMARY KEY,
    user_id 		 BIGINT UNIQUE,
    name             TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.poi (
	id               SERIAL PRIMARY KEY,
    poi_id 			 BIGINT UNIQUE,
    name             TEXT NOT NULL,
	lat			  	 TEXT,
	long			 TEXT
);

CREATE TABLE IF NOT EXISTS public.maintenance (
	id               SERIAL PRIMARY KEY,
    feedback_id 	 BIGINT UNIQUE,
    trail_name       TEXT NOT NULL,
	comment			 TEXT,
	lat			  	 TEXT,
	long			 TEXT
);

