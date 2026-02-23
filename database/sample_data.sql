-- Adds pseudo reviews

--Populating trail names
INSERT INTO pa.trails (trail_name)
SELECT name
FROM strava.trails
ON CONFLICT DO NOTHING;

--Populating usernames
INSERT INTO pa.users (username)
VALUES
    ('MARIE'),
    ('CHRIS'),
    ('ADEBOLA'),
    ('DORA'),
    ('AFONSO'),
    ('DENI'),
    ('VIJAY'),
    ('TILAK'),
    ('OM'),
    ('SANTI'),
    ('BELEN'),
    ('RICARDO'),
    ('BEKOO'),
    ('ALEXANDER'),
    ('MARCO'),
    ('KANA'),
    ('CAMMY'),
    ('SABA'),
    ('WILMA');

--Populating trail ratings
INSERT INTO pa.trail_ratings (trail_name, rating, comment, username) -- how to connect pa.users to pa.trail_ratings
VALUES 
    ('Rib Machico - Portela',5, 'Amazing trail! Perfect views and well-maintained.', 'MARIE'),
    ('Trilho Sandokan',4, 'A bit steep, but totally worth the effort.', 'CHRIS'),
    ('Pista do Aeroporto',3, 'Average experience, could use some maintenance.', 'ADEBOLA'),
    ('parte final Redline',5, 'Absolutely loved it! Would come again.', 'DORA'),
    ('Marginal Ribeira Brava Sentido Oeste',2, 'Too crowded and not as scenic as expected.', 'AFONSO'),
    ('landeiros / rib mx',4, 'Great trail, but parking was limited.', 'DENI'),
    ('Prazeres-Fajã da ovelha (VR3)',5, 'Best trail I have ever visited! Highly recommended.', 'VIJAY'),
    ('Santa do Porto Moniz - Ponta do Pargo',2, 'Trail was okay but needs better signage.', 'TILAK'),
    ('Top Speed - Meia Légua',4, 'Really enjoyed the challenge of this trail.', 'OM'),
    ('Santa do Porto Moniz - Ponta do Pargo',1, 'Horrible experience, trail was closed without notice.', 'SANTI'),
    ('parte final Redline',3, 'Decent ride, but not very memorable.', 'BELEN'),
    ('Túnel - Caniçal',5, 'Loved the sunrise from this trail.', 'RICARDO'),
    ('Subida da Azenha no Caniço',2, 'Miyav', 'BEKOO'),
    ('Madalena: cruzamento - rotunda',2, 'Could be better', 'ALEXANDER'),
    ('ER208 Climb',2, 'Not bumpy enough', 'MARCO'),
    ('Câmara de Lobos - Estreito Câmara Lobos',2, 'Not my favorite, too crowded on weekends.', 'KANA'),
    ('Beer Garden Climb',2, 'Wished it was longer', 'CAMMY'),
    ('Campanario - Cabo Girao',2, 'Woooooo', 'SABA'),
    (' Pináculo fim da Conde Carvalhal',5, 'Perfect for an afternoon ride. Great upkeep!', 'WILMA');

--Populating maintenance requests
INSERT INTO pa.maintenance (trail_name, maint_comment)
VALUES 
    ('Trilho Sandokan', 'Landslide'),
    ('Santo da Serra - Camacha', 'Needs smoothing'),
    ('Rotunda a Rotunda', 'Tree across trail'),
    ('Subida Rosário/Encumeada', 'Heavily flooded'),
    ('Rotunda Hotel - Rotunda Arco da Calheta', 'Jagged rocks'),
    ('Marginal Ribeira Brava Sentido Oeste', 'Fallen tree branch'),
    ('ER110 Climb', 'Dead animal'),
    ('Câmara de Lobos - Estreito Câmara Lobos', 'Flooded'),
    ('landeiros / rib mx', 'Flooded'),
    ('Volta da praia', 'Tree across trail'),
    ('Pico de Arieiro car park smash', 'Rocks');