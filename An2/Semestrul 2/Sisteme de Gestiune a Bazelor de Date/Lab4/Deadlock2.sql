-- SET DEADLOCK_PRIORITY LOW

BEGIN TRAN

UPDATE PacheteTuristice SET Pret = '2.99'
WHERE NumePachet = 'Vacanta la Paris';

WAITFOR DELAY '00:00:10'

UPDATE Clienti SET Telefon = '0700000002'
WHERE Nume = 'Popescu';

COMMIT TRAN