-- User table
INSERT INTO public.users(first_name, last_name, email)
VALUES
('Andrei', 'Popescu', 'andrei_popescu@email.email'),
('Tudor', 'Munteanu', 'tudor_munteanu@email.email'),
('Ana', 'Dumitrescu', 'ana_dumitrescu@email.email'),
('Gabriela', 'Stanescu', 'gabriela_stanescu@email.email'),
('Cristian', 'Gheran', 'cristian_gheran@email.email'),
('Raluca', 'Pop', 'raluca_pop@email.email'),
('Luca', 'Dunca', 'luca_dunca@email.email');

DELETE FROM users

SELECT * FROM users



-- Friendship table
INSERT INTO public.friendships(friends_from, user1_id, user2_id, friendRequestStatus)
VALUES
('2023-11-16 15:30:14', (select id from users where email='andrei_popescu@email.email'), (select id from users where email='ana_dumitrescu@email.email'), 'ACCEPTED'),
('2023-05-15 17:32:49', (select id from users where email='andrei_popescu@email.email'), (select id from users where email='raluca_pop@email.email'), 'ACCEPTED'),
('2023-11-03 07:30:00', (select id from users where email='luca_dunca@email.email'), (select id from users where email='cristian_gheran@email.email'), 'ACCEPTED'),
('2023-09-12 14:53:28', (select id from users where email='cristian_gheran@email.email'), (select id from users where email='gabriela_stanescu@email.email'), 'ACCEPTED'),
('2023-10-28 20:14:37', (select id from users where email='gabriela_stanescu@email.email'), (select id from users where email='tudor_munteanu@email.email'), 'ACCEPTED');

DELETE  FROM friendships

SELECT * FROM friendships