DROP TABLE IF EXISTS pa.users;

CREATE TABLE IF NOT EXISTS pa.users (
	id               SERIAL,
    username         varchar(255) NOT NULL PRIMARY KEY
    --username will first be initially populated here as well then?
);

DROP TABLE IF EXISTS pa.trails;

CREATE TABLE IF NOT EXISTS pa.trails(
	id               SERIAL,
    trail_name       varchar(255) NOT NULL PRIMARY KEY
    -- would be good if link this to the strava trail names
);

DROP TABLE IF EXISTS pa.trail_ratings;

CREATE TABLE IF NOT EXISTS pa.trail_ratings (
	id         SERIAL PRIMARY KEY,
    trail_name   varchar(255) NOT NULL REFERENCES pa.trails(trail_name),
    -- would be good if we can autopopulate trail name based on strava info
	rating      INTEGER CHECK (rating BETWEEN 1 AND 5),
	username    varchar(255) NOT NULL REFERENCES pa.users(username),
    comment     varchar,
	created_at  TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS pa.maintenance;

CREATE TABLE IF NOT EXISTS pa.maintenance (
	id               SERIAL PRIMARY KEY,
    trail_name      varchar(255) NOT NULL REFERENCES pa.trails(trail_name),
    -- would be good if we can autopopulate trail name based on strava info
	maint_comment	 varchar,
);