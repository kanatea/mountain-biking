-- Data processing - transforming climb_category_desc in the strava trails table for clearer labeling on the frontend

-- Definition of climb category: A segment can be categorized as a climb on Strava if the length of the climb (in meters) 
-- multiplied by the grade of the climb is greater than 8,000

Update strava.trails SET climb_category_desc = 'Not Categorized' WHERE climb_category=0;
UPDATE strava.trails SET climb_category_desc = 'Category 4' WHERE climb_category=1;
UPDATE strava.trails SET climb_category_desc = 'Category 3' WHERE climb_category=2;
UPDATE strava.trails SET climb_category_desc = 'Category 2' WHERE climb_category=3;
UPDATE strava.trails SET climb_category_desc = 'Category 1' WHERE climb_category=4;
UPDATE strava.trails SET climb_category_desc = 'Hors Catégorie' WHERE climb_category=5;

