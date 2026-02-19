-- A segment can be categorized as a climb on Strava
-- if the length of the climb (in meters) multiplied 
-- by the grade of the climb is greater than 8,000.

ALTER TABLE strava.trails
DROP IF EXISTS climb_grade;

ALTER TABLE strava.trails
ADD climb_grade TEXT;

Update strava.trails SET climb_grade = 'Not Categorized (Beginner)' WHERE climb_category=0;
UPDATE strava.trails SET climb_grade = 'Easy' WHERE climb_category=1;
UPDATE strava.trails SET climb_grade = 'Easy - Intermediate' WHERE climb_category=2;
UPDATE strava.trails SET climb_grade = 'Intermediate - Difficult' WHERE climb_category=3;
UPDATE strava.trails SET climb_grade = 'Difficult' WHERE climb_category=4;
UPDATE strava.trails SET climb_grade = 'Expert (Hors Catégorie)' WHERE climb_category=5;