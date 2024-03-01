use Calatorii
go

-- Clienti
INSERT INTO Clienti (IDClient, Nume, Prenume, Email, Telefon)
VALUES 
(1, 'Popescu', 'Andrei', 'popescu.andrei@example.com', '0712345678'),
(2, 'Dumitrescu', 'Ana-Maria', 'dumitrescu.anamaria@example.com', '0798765432'),
(3, 'Munteanu', 'Tudor', 'munteanu.tudor@example.com', '0755555555'),
(4, 'Stanescu', 'Gabriela', 'stanescu.gabriela@example.com', '0711111111'),
(5, 'Gheran', 'Cristian', 'gheran.cristian@example.com', '0799999999');

-- Destinatii
INSERT INTO Destinatii (IDDestinatie, NumeDestinatie, Descriere, Tara, Oras)
VALUES
(1, 'Paris', 'Capitala Frantei', 'Franta', 'Paris'),
(2, 'Roma', 'Capitala Italiei', 'Italia', 'Roma'),
(3, 'Barcelona', 'Oras situat pe coasta mediteraneeana', 'Spania', 'Barcelona'),
(4, 'Viena', 'Capitala Austriei', 'Austria', 'Viena'),
(5, 'Atena', 'Capitala Greciei', 'Grecia', 'Atena');

-- PacheteTusistice
INSERT INTO PacheteTuristice (IDPachetTuristic, NumePachet, Descriere, Pret, DestinatieID)
VALUES
(1, 'Vacanta la Paris', 'Descoperiti frumusetea Parisului', 1500.00, 1),
(2, 'Minisejur la Roma', 'Exploreaza Roma in 4 zile', 1200.00, 2),
(3, 'Sejur in Barcelona', 'Plaja si distractie in Barcelona', 1800.00, 3),
(4, 'Orasul Muzicii - Viena', 'Descoperiti cultura si muzica din Viena', 1700.00, 4),
(5, 'Aventura in Atena', 'Exploreaza istoria Greciei', 1600.00, 5);

-- Rezervarii
-- DELETE FROM Rezervari
INSERT INTO Rezervari (IDRezervare, DataInceput, DataSfarsit, ClientID, PachetID)
VALUES
(1, '2023-05-15', '2023-05-22', 1, 1),
(2, '2023-06-10', '2023-06-17', 2, 2),
(3, '2023-07-01', '2023-07-08', 3, 3),
(4, '2023-07-20', '2023-07-27', 4, 5),
(5, '2023-08-05', '2023-08-12', 5, 5);

-- Transporturi
INSERT INTO Transporturi (IDTransport, TipTransport, CompanieTransport, PretBilet, PachetID)
VALUES
(1, 'Avion', 'Air France', 600.00, 1),
(2, 'Tren', 'Trenitalia', 80.00, 2),
(3, 'Avion', 'Iberia', 350.00, 3),
(4, 'Tren', 'OBB', 120.00, 4),
(5, 'Avion', 'Aegean Airlines', 400.00, 5);

-- Hoteluri
INSERT INTO Hoteluri (IDHotel, NumeHotel, Stele, Adresa, PretCamera, PachetID)
VALUES
(1, 'Hotel Eiffel', 4, '123 Rue de la Tour, Paris', 200.00, 1),
(2, 'Hotel Romanico', 3, '456 Via Nazionale, Roma', 150.00, 2),
(3, 'Barcelona Beach Hotel', 4, '789 Beachfront Blvd, Barcelona', 220.00, 3),
(4, 'Hotel Imperial', 5, '101 Ringstrasse, Viena', 250.00, 4),
(5, 'Acropolis View Hotel', 4, '321 Parthenon Avenue, Atena', 210.00, 5);

-- CamereHotel
INSERT INTO CamereHotel (IDCameraHotel, TipCamera, Capacitate, PretNoapte, HotelID)
VALUES
(1, 'Camera Dubla', 2, 100.00, 1),
(2, 'Camera Single', 1, 80.00, 2),
(3, 'Camera cu vedere la mare', 2, 120.00, 3),
(4, 'Camera Deluxe', 2, 150.00, 4),
(5, 'Camera cu vedere la Acropole', 2, 110.00, 5);

-- Plati
-- DELETE FROM Plati
INSERT INTO Plati (IDPlata, SumaPlata, DataPlata, MetodaPlata, RezervareID)
VALUES
(1, 800.00, '2023-03-01', 'Card de credit', 1),
(2, 1200.00, '2023-04-15', 'PayPal', 2),
(3, 1500.00, '2023-05-10', 'Card de credit', 3),
(5, 1400.00, '2023-07-15', 'Transfer bancar', 5);
-- (4, 1000.00, '2023-06-05', 'Card de credit', 4),

-- ExcursiiOptionale
INSERT INTO ExcursiiOptionale (IDExcursie, NumeExcursie, Descriere, Pret, PachetID)
VALUES
(1, 'Turul Turnului Eiffel', 'Vizitati cele mai frumoase puncte de pe Turnul Eiffel', 50.00, 1),
(2, 'Excursie la Colosseum', 'Exploreaza minunatul Colosseum din Roma', 40.00, 2),
(3, 'Turul Sagrada Familia', 'Vizitati capodopera lui Gaudi in Barcelona', 60.00, 3),
(4, 'Concert la Opera din Viena', 'Bucurati-va de muzica clasica la Opera din Viena', 70.00, 4),
(5, 'Turul Acropolei', 'Descoperiti istoria Greciei la Acropole', 45.00, 5);

-- RecenziiClienti
-- DELETE FROM RecenziiClienti
INSERT INTO RecenziiClienti (ClientID, PachetID, TextRecenzie, Rating, DataRecenzie)
VALUES
(1, 1, 'Vacanta minunata! Servicii excelente.', 5, '2023-06-30'),
(3, 3, 'Barcelona a fost superba!', 4, '2023-07-20'),
(2, 2, 'Roma este plina de istorie.', 4, '2023-08-10'),
(4, 3, 'Barcelona este spectaculoasa si plina de viata.', 4, '2023-07-25'),
(5, 5, 'Atena este plina de mitologie.', 4, '2023-08-05');
--(1, 4, 'Targul de Craciun din Viena este o experienta de neratat.', 5, '2022-12-16');

-- select
select * from Clienti
select * from Destinatii
select * from PacheteTuristice
select * from Rezervari
select * from Transporturi
select * from Hoteluri
select * from CamereHotel
select * from Plati
select * from ExcursiiOptionale
select * from RecenziiClienti