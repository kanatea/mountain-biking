-- Create tables for the pa schema, storing the information from the users, trail ratings/reviews, and any reported problems/maintenance issues

DROP TABLE IF EXISTS pa.users;
-- Stores user info
CREATE TABLE IF NOT EXISTS pa.users (
	id               SERIAL,
    username         varchar(255) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS pa.trails;
-- Stores trail name that is reviewed or reported (limited to what exists from the strava dataset, 
-- this constraint is reinforced from the frontend by limiting the input trail names
CREATE TABLE IF NOT EXISTS pa.trails(
	id               SERIAL,
    trail_name       varchar(255) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS pa.trail_ratings;
-- Stores trail ratings, which includes a 1-5 star rating (stored as an integer), and a comment/review on the trail itself
-- Timestamp to display the most recent comment
CREATE TABLE IF NOT EXISTS pa.trail_ratings (
	id         SERIAL PRIMARY KEY,
    trail_name   varchar(255) NOT NULL REFERENCES pa.trails(trail_name),
	rating      INTEGER CHECK (rating BETWEEN 1 AND 5),
	username    varchar(255) NOT NULL REFERENCES pa.users(username),
    comment     varchar,
	created_at  TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS pa.maintenance;
-- Allows users to report any problems or maintenance issues on specific trails
-- Timestamp to display the most recent problem
CREATE TABLE IF NOT EXISTS pa.maintenance (
	id               SERIAL PRIMARY KEY,
    trail_name      varchar(255) NOT NULL REFERENCES pa.trails(trail_name),
	maint_comment	 varchar,
	created_at       TIMESTAMP DEFAULT NOW()
);


