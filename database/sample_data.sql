-- Adds pseudo reviews
-- Tables: pa.trail_ratings, pa.users, pa.poi, pa.maintenance

INSERT INTO pa.users (username)
VALUES 
    ('johndoe'),
    ('janedoe'),
    ('trailblazer99'),
    ('mountainlover'),
    ('biker5000'),
    ('naturefanatic'),
    ('adventureguy');

INSERT INTO pa.trails(trail_id)
VALUES 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6);

INSERT INTO pa.trail_ratings (trail_id, rating, comment, username) -- how to connect pa.users to pa.trail_ratings
VALUES 
    (6, 5, 'Amazing trail! Perfect views and well-maintained.', 'johndoe'),
    (2, 4, 'A bit steep, but totally worth the effort.', 'janedoe'),
    (3, 3, 'Average experience, could use some maintenance.', 'trailblazer99'),
    (6, 5, 'Absolutely loved it! Would come again.', 'mountainlover'),
    (2, 2, 'Too crowded and not as scenic as expected.', 'biker5000'),
    (3, 4, 'Great trail, but parking was limited.', 'naturefanatic'),
    (4, 5, 'Best trail I have ever visited! Highly recommended.', 'adventureguy'),
    (3, 2, 'Trail was okay but needs better signage.', 'johndoe'),
    (4, 4, 'Really enjoyed the challenge of this trail.', 'janedoe'),
    (5, 1, 'Horrible experience, trail was closed without notice.', 'trailblazer99'),
    (2, 3, 'Decent ride, but not very memorable.', 'naturefanatic'),
    (6, 5, 'Loved the sunrise from this trail. A must-visit!', 'adventureguy'),
    (6, 2, 'Not my favorite, too crowded on weekends.', 'biker5000'),
    (2, 5, 'Perfect for an afternoon ride. Great upkeep!', 'mountainlover');

INSERT INTO pa.maintenance (trail_id, maint_comment)
VALUES 
    (4, 'Rocks'),
    (6, 'Needs smoothing'),
    (3, 'Flooded'),
    (5, 'Rocks');