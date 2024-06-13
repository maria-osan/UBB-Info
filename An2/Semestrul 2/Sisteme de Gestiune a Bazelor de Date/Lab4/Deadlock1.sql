SET DEADLOCK_PRIORITY LOW

BEGIN TRAN

UPDATE Clienti SET Telefon = '0700000001'
WHERE Nume = 'Popescu';

WAITFOR DELAY '00:00:10'

UPDATE PacheteTuristice SET Pret = '1.99'
WHERE NumePachet = 'Vacanta la Paris';

COMMIT TRAN


SELECT * FROM Clienti
SELECT * FROM PacheteTuristice

UPDATE Clienti SET Telefon = '0712345678'
WHERE Nume = 'Popescu';
UPDATE PacheteTuristice SET Pret = '1700'
WHERE NumePachet = 'Vacanta la Paris';