INSERT INTO Clienti (IDClient, Nume, Prenume, Telefon, Email)
VALUES ((SELECT ISNULL(MAX(IDClient), 0) + 1 FROM Clienti), 'Sava', 'Ana', '0722222222', 'ana@email.com')

BEGIN TRAN
WAITFOR DELAY '00:00:10'
UPDATE Clienti SET Prenume = 'David'
WHERE Nume = 'Sava'
COMMIT TRAN


DELETE FROM Clienti WHERE Nume = 'Sava'
SELECT * FROM Clienti