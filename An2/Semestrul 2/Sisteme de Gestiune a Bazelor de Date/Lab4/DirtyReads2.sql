-- SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
SELECT * FROM Clienti
WAITFOR DELAY '00:00:15'
SELECT * FROM Clienti
COMMIT TRAN