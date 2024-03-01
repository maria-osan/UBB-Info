ALTER TABLE users
ADD COLUMN password CHARACTER VARYING(50);

UPDATE users
SET password = 'andrei123'
WHERE id = 1;

UPDATE users
SET password = '1a2b3c'
WHERE id = 2;

UPDATE users
SET password = '1234a'
WHERE id = 3;

UPDATE users
SET password = '321'
WHERE id = 4;

UPDATE users
SET password = '1'
WHERE id = 5;

UPDATE users
SET password = 'RalucaPassword'
WHERE id = 6;

UPDATE users
SET password = 'LucaDunca'
WHERE id = 7;

UPDATE users
SET password = 'a'
WHERE id = 11;

UPDATE users
SET password = 'b'
WHERE id = 12;

UPDATE users
SET password = 'c'
WHERE id = 13;


DELETE FROM users

SELECT * FROM users