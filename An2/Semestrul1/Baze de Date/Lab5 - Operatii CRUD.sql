-- Tabele: Clienti - Rezervari - PacheteTuristice (relatie many - to - many)

-- NOT NULL
CREATE OR ALTER FUNCTION IN_NOT_NULL(@string varchar(100))
	RETURNS INT
AS
BEGIN
	IF @string IS NOT NULL
	BEGIN
		RETURN 1
	END

	RETURN 0
END
GO

-- Validare Telefon
CREATE OR ALTER FUNCTION IS_VALID_Telefon (@televon varchar(20))
	RETURNS INT
AS
BEGIN
	IF (LEN(@televon) = 10)
	BEGIN
		RETURN 1
	END

	RETURN 0
END
GO

-- Validare ID Clienti
CREATE OR ALTER FUNCTION IS_VALID_IDClienti(@idClient INT)
	RETURNS INT
AS
BEGIN
	IF EXISTS (SELECT * FROM Clienti WHERE @idClient = Clienti.IDClient)
	BEGIN
		RETURN 1
	END

	RETURN 0
END
GO


--- CRUD pentru Clienti ---
CREATE OR ALTER PROCEDURE CRUD_Clienti
	@nume varchar(100),
	@prenume varchar(100),
	@email varchar(100),
	@telefon varchar(20),
	@nr_rows INT = 1
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @last_id INT = (SELECT MAX(Clienti.IDClient) FROM Clienti);
	DECLARE @id INT;
	SET @id = @last_id + 1;

	IF (dbo.IN_NOT_NULL(@nume) = 1 AND
		dbo.IN_NOT_NULL(@prenume) = 1 AND
		dbo.IN_NOT_NULL(@email) = 1 AND
		dbo.IN_NOT_NULL(@telefon) = 1 AND
		dbo.IS_VALID_Telefon(@telefon) = 1)
	BEGIN
		-- INSERT
		DECLARE @n INT = 0;
		WHILE (@n < @nr_rows)
		BEGIN
			INSERT INTO Clienti VALUES (@id, @nume, @prenume, @email, @telefon);
			SET @id = @id + 1;
			SET @n = @n + 1;
		END

		-- SELECT
		SELECT * FROM Clienti ORDER BY Clienti.Nume;

		-- UPDATE
		UPDATE Clienti
		SET Clienti.Nume = @nume + '_CRUD'
		WHERE Clienti.Nume = @nume;

		SELECT * FROM Clienti;

		-- DELETE
		DELETE FROM Clienti
		WHERE Clienti.Nume LIKE @nume + '_CRUD';

		SELECT * FROM Clienti;

		PRINT 'Operatiile CRUD pentru Clienti au fost efectuate.';
	END

	ELSE
	BEGIN
		RAISERROR('Datele de intrare nu sunt valide.', 16, 1);
	END
END
GO

SELECT * FROM Clienti;
EXEC CRUD_Clienti 'Test', 'Test', 'test@example.com', '0701234567', 3;


GO

-- Validare ID Destinatii
CREATE OR ALTER FUNCTION IS_VALID_IDDesctinatii(@idDestinatie INT)
	RETURNS INT
AS
BEGIN
	IF EXISTS (SELECT * FROM Destinatii WHERE @idDestinatie = Destinatii.IDDestinatie)
	BEGIN
		RETURN 1
	END

	RETURN 0
END
GO

-- Validare Pret
CREATE OR ALTER FUNCTION IS_VALID_Pret (@pret DECIMAL(10, 2))
	RETURNS INT
AS
BEGIN
	IF @pret BETWEEN 0.00 AND 999999.99
	BEGIN
		RETURN 1
	END

	RETURN 0
END
GO


--- CRUD pentru PacheteTuristice ---
CREATE OR ALTER PROCEDURE CRUD_PacheteTuristice
	@nume_pachet varchar(100),
	@descriere varchar(100),
	@pret decimal(10, 2),
	@id_destinatie INT,
	@nr_rows INT = 1
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @last_id INT = (SELECT MAX(PacheteTuristice.IDPachetTuristic) FROM PacheteTuristice);
	DECLARE @id INT;
	SET @id = @last_id + 1;

	IF (dbo.IN_NOT_NULL(@nume_pachet) = 1 AND
		dbo.IN_NOT_NULL(@descriere) = 1 AND 
		dbo.IS_VALID_Pret(@pret) = 1 AND
		dbo.IS_VALID_IDDesctinatii(@id_destinatie) = 1)
	BEGIN
		-- INSERT
		DECLARE @n INT = 0;
		WHILE (@n < @nr_rows)
		BEGIN
			INSERT INTO PacheteTuristice VALUES (@id, @nume_pachet, @descriere, @pret, @id_destinatie);
			SET @id = @id + 1;
			SET @n = @n + 1;
		END

		-- SELECT
		SELECT * FROM PacheteTuristice ORDER BY PacheteTuristice.NumePachet;

		-- UPDARE
		UPDATE PacheteTuristice
		SET PacheteTuristice.NumePachet = @nume_pachet + '_CRUD'
		WHERE PacheteTuristice.NumePachet = @nume_pachet;

		SELECT * FROM PacheteTuristice ORDER BY PacheteTuristice.NumePachet;

		-- DELET
		DELETE FROM PacheteTuristice
		WHERE PacheteTuristice.NumePachet LIKE @nume_pachet + '_CRUD';

		SELECT * FROM PacheteTuristice ORDER BY PacheteTuristice.NumePachet;

		PRINT 'Operatiile CRUD pentru PacheteTuristice au fost efectuate.';
	END

	ELSE
	BEGIN
		RAISERROR('Datele de intrare nu sunt valide.', 16, 1);
	END
END
GO

SELECT * FROM PacheteTuristice;
EXEC CRUD_PacheteTuristice 'Test', 'Test test', 1265.00, 3, 3;


GO

-- Validare ID PacheteTuristice
CREATE OR ALTER FUNCTION IS_VALID_IDPacheteTuristice(@idPachetTuristic INT)
	RETURNS INT
AS
BEGIN
	IF EXISTS (SELECT * FROM PacheteTuristice WHERE @idPachetTuristic = PacheteTuristice.IDPachetTuristic)
	BEGIN
		RETURN 1
	END

	RETURN 0
END
GO


--- CRUD pentru Rezervari ---
CREATE OR ALTER PROCEDURE CRUD_Rezervari
	@data_inceput DATE,
	@data_sfarsit DATE,
	@id_client INT,
	@id_pachetTuristic INT
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @last_id INT = (SELECT MAX(PacheteTuristice.IDPachetTuristic) FROM PacheteTuristice);
	DECLARE @id INT;
	SET @id = @last_id + 1;

	IF (@data_inceput IS NOT NULL AND
		@data_sfarsit IS NOT NULL AND
		dbo.IS_VALID_IDClienti(@id_client) = 1 AND
		dbo.IS_VALID_IDPacheteTuristice(@id_pachetTuristic) = 1)
	BEGIN
		-- INSERT
		INSERT INTO Rezervari VALUES (@id, @data_inceput, @data_sfarsit, @id_client, @id_pachetTuristic);

		-- SELECT
		SELECT * FROM Rezervari ORDER BY Rezervari.DataInceput;

		-- UPDATE
		UPDATE Rezervari
		SET Rezervari.ClientID = @id_client + 1
		WHERE Rezervari.ClientID = @id_client;

		SELECT * FROM Rezervari ORDER BY Rezervari.ClientID;

		-- DELETE
		DELETE FROM Rezervari
		WHERE Rezervari.ClientID = @id_client + 1 AND Rezervari.PachetID = @id_pachetTuristic;

		SELECT * FROM Rezervari ORDER BY Rezervari.ClientID;

		PRINT 'Operatiile CRUD pentru Rezervari au fost efectuate.';
	END

	ELSE
	BEGIN
		RAISERROR('Datele de intrare nu sunt valide.', 16, 1);
	END
END
GO

SELECT * FROM Rezervari;
EXEC CRUD_Rezervari '2023-11-29', '2023-12-06', 4, 4;


GO

------ Views ------
CREATE OR ALTER VIEW View_PacheteTuristice
AS
	SELECT  PT.NumePachet, PT.Pret
	FROM PacheteTuristice AS PT
	INNER JOIN Destinatii AS D
	ON PT.DestinatieID = D.IDDestinatie
	WHERE PT.Pret > 1500.00;
GO

SELECT * FROM View_PacheteTuristice;
GO

CREATE OR ALTER VIEW View_Rezervari
AS
	SELECT C.Nume, C.Prenume, PT.NumePachet, PT.Pret, R.DataInceput, R.DataSfarsit
	FROM Rezervari AS R
	INNER JOIN Clienti AS C
	ON R.ClientID = C.IDClient
	INNER JOIN PacheteTuristice AS PT
	ON R.PachetID = PT.IDPachetTuristic;
GO

SELECT * FROM View_Rezervari;
GO


------ INDEXI ------
-- Clienti
CREATE NONCLUSTERED INDEX N_idx_Nume ON Clienti (Nume);
CREATE NONCLUSTERED INDEX N_idx_Prenume ON Clienti (Prenume);
CREATE NONCLUSTERED INDEX N_idx_IDClient ON Clienti (IDClient);

-- PacheteTuristice
CREATE NONCLUSTERED INDEX N_idx_NumePachet ON PacheteTuristice (NumePachet);
CREATE NONCLUSTERED INDEX N_idx_Pret ON PacheteTuristice (Pret);
CREATE NONCLUSTERED INDEX N_idx_IDPachetTuristic ON PacheteTuristice (IDPachetTuristic);

-- Rezervari
CREATE NONCLUSTERED INDEX N_idx_DataInceput ON Rezervari (DataInceput);
CREATE NONCLUSTERED INDEX N_idx_DataSfarsit ON Rezervari (DataSfarsit);
CREATE NONCLUSTERED INDEX N_idx_IDClient ON Rezervari (ClientID);
CREATE NONCLUSTERED INDEX N_idx_IDPachetTuristic ON Rezervari (PachetID);

-- Drop
DROP INDEX N_idx_Nume ON Clienti;
DROP INDEX N_idx_Prenume ON Clienti;
DROP INDEX N_idx_IDClient ON Clienti;
DROP INDEX N_idx_NumePachet ON PacheteTuristice;
DROP INDEX N_idx_Pret ON PacheteTuristice;
DROP INDEX N_idx_IDPachetTuristic ON PacheteTuristice;
DROP INDEX N_idx_DataInceput ON Rezervari;
DROP INDEX N_idx_DataSfarsit ON Rezervari;
DROP INDEX N_idx_IDClient ON Rezervari;
DROP INDEX N_idx_IDPachetTuristic ON Rezervari;

SELECT * FROM View_PacheteTuristice;
SELECT * FROM View_Rezervari;