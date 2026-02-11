DROP TABLE IF EXISTS p.trails
	p as in public;

CREATE TABLE p.trails (
	id               SERIAL PRIMARY KEY,
    strava_segment_id BIGINT UNIQUE,
    name             TEXT NOT NULL,
    distance_m       INTEGER,
    elevation_gain_m INTEGER,
    average_grade    NUMERIC,
    start_point      TEXT,
    end_point        TEXT
);


CREATE TABLE IF NOT EXISTS p.trail_ratings (
	id SERIAL PRIMARY KEY,
	trail_id INTEGER REFERENCES trails(id) ON DELETE CASCADE,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	created_at TIMESTAMP DEFAULT NOW()
);

