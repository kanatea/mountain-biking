DROP TABLE IF EXISTS pa.users;

CREATE TABLE IF NOT EXISTS pa.users (
	id               SERIAL,
    username         varchar(255) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS pa.trails;

CREATE TABLE IF NOT EXISTS pa.trails(
	id               SERIAL,
    trail_name       varchar(255) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS pa.trail_ratings;

CREATE TABLE IF NOT EXISTS pa.trail_ratings (
	id         SERIAL PRIMARY KEY,
    trail_name   varchar(255) NOT NULL REFERENCES pa.trails(trail_name),
	rating      INTEGER CHECK (rating BETWEEN 1 AND 5),
	username    varchar(255) NOT NULL REFERENCES pa.users(username),
    comment     varchar,
	created_at  TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS pa.maintenance;

CREATE TABLE IF NOT EXISTS pa.maintenance (
	id               SERIAL PRIMARY KEY,
    trail_name      varchar(255) NOT NULL REFERENCES pa.trails(trail_name),
	maint_comment	 varchar,
);
