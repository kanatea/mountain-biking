-- Database: madeira_trails

-- DROP DATABASE IF EXISTS madeira_trails;

CREATE DATABASE madeira_trails
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United Kingdom.1252'
    LC_CTYPE = 'English_United Kingdom.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE trails (
    id               SERIAL PRIMARY KEY,
    strava_segment_id BIGINT UNIQUE,
    name             TEXT NOT NULL,
    distance_m       INTEGER,
    elevation_gain_m INTEGER,
    average_grade    NUMERIC,
    start_point      TEXT,
    end_point        TEXT
);




CREATE TABLE IF NOT EXISTS trail_ratings (
	id SERIAL PRIMARY KEY,
	trail_id INTEGER REFERENCES trails(id) ON DELETE CASCADE,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	created_at TIMESTAMP DEFAULT NOW()
);

