BEGIN TRAN
WAITFOR DELAY '00:00:10'
INSERT INTO Clienti (IDClient, Nume, Prenume, Telefon, Email)
VALUES ((SELECT ISNULL(MAX(IDClient), 0) + 1 FROM Clienti), 'Phantom', 'Reads', '0733333333', 'reads@email.com')
COMMIT TRAN


DELETE FROM Clienti WHERE Nume = 'Phantom'
SELECT * FROM Clienti