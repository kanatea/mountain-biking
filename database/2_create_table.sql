DROP TABLE IF EXISTS strava.trails;

CREATE TABLE IF NOT EXISTS strava.trails
(
    id integer NOT NULL DEFAULT nextval('strava.trails_id_seq'::regclass),
    strava_segment_id bigint,
    name text COLLATE pg_catalog."default" NOT NULL,
    region text COLLATE pg_catalog."default" DEFAULT 'Madeira'::text,
    distance_m integer,
    elevation_gain_m integer,
    avg_grade numeric,
    created_at timestamp without time zone DEFAULT now(),
    start_lat double precision,
    start_lon double precision,
    end_lat double precision,
    end_lon double precision,
    polyline text COLLATE pg_catalog."default",
    climb_category integer,
    climb_category_desc text COLLATE pg_catalog."default",
    CONSTRAINT trails_pkey PRIMARY KEY (id),
    CONSTRAINT trails_strava_segment_id_key UNIQUE (strava_segment_id)
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

