SELECT * FROM dojos;
SELECT * FROM ninjas;

# Create 3 new dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES /*1*/("Kinjaz Studio", NOW(), Now()), /*2*/("Dojo Coders", NOW(), NOW()), /*3*/("Four Elements", NOW(), NOW());

# Delete the 3 dojos
DELETE FROM dojos;

# Create 3 more dojos
INSERT INTO dojos (name, created_at, updated_at)
Values /*1*/("Re:Samurai Effect", NOW(), NOW()), /*2*/("Shikigami Users", NOW(), NOW()), /*3*/("Spellbind Dojo", NOW(), NOW());

# Create 3 ninjas that belong to the 1st dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES /*1*/("Furuta", "Higami", 24, NOW(), NOW(), 4), /*2*/("Ken", "Watanabe", 39, NOW(), NOW(), 4), /*3*/("Hiroyuki", "Sanada", 62, NOW(), NOW(), 4);

# Create 3 ninjas that belong to the 2nd dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES /*1*/("Aki", "Dazai", 55, NOW(), NOW(), 5), /*2*/("Kong", "Li", 30, NOW(), NOW(), 5), /*3*/("Haruki", "Ito", 21, NOW(), NOW(), 5);

# Create 3 ninjas that belong to the 3rd dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES /*1*/("Inu", "Maki", 23, NOW(), NOW(), 6), /*2*/("Jet", "Xihyuo", 45, NOW(), NOW(), 6), /*3*/("Ichigo", "Fushiguro", 29, NOW(), NOW(), 6);

# Retreive all the ninjas from the 1st dojo
SELECT * FROM ninjas WHERE dojo_id = 4;

# Retreive all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 6;

# Retreive the last ninja's dojo
SELECT * FROM dojos WHERE id = 6;