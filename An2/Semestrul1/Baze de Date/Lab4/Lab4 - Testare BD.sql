use Calatorii

/*
Clienti: 1 Pk, no FK - 1 table
ExcursiiOptionale: 1 PK + FK - 2 tables
RecenziiClienti: 2 PK - 2 tables + GROUP BY
*/

-- Table Tables - with the name of the tables considered
INSERT INTO Tables (Name)
VALUES
	('Clienti'),
	('ExcursiiOptionale'),
	('RecenziiClienti');

SELECT * FROM Tables

DELETE FROM Tables
GO


ALTER TABLE RecenziiClienti
ADD CONSTRAINT FK_ClientID FOREIGN KEY (ClientID) REFERENCES Clienti(IDClient) ON DELETE CASCADE;


-- Table Views – with the names of the views considered (not necessarily created on the tables
-- considered in the table Tables, but preferable to see the time results)

-- for one PK, no FK
CREATE VIEW View_Clienti AS
	SELECT * FROM Clienti
GO

-- for one PK + FK
CREATE VIEW View_ExcursiiOptionale AS
	SELECT eo.NumeExcursie, eo.Pret
	FROM ExcursiiOptionale eo
	INNER JOIN PacheteTuristice pt ON eo.PachetID = pt.IDPachetTuristic
GO

-- for two PK
CREATE VIEW View_RecenziiClienti AS
	SELECT c.Nume, c.Prenume, r.Rating, r.TextRecenzie, r.DataRecenzie
	FROM RecenziiClienti r
	INNER JOIN Clienti c ON r.ClientID = c.IDClient
	INNER JOIN PacheteTuristice pt ON r.PachetID = pt.IDPachetTuristic
	GROUP BY c.Nume, c.Prenume, r.Rating, r.TextRecenzie, r.DataRecenzie
GO

-- Adaug view-urile in tabela Views
INSERT INTO Views (Name)
VALUES
	('View_Clienti'),
	('View_ExcursiiOptionale'),
	('View_RecenziiClienti');

SELECT * FROM Views

DELETE FROM Views


-- Adaug testele de efectuat in tabela Tests
INSERT INTO Tests (Name)
VALUES
	('DIV_Clienti_10'),
	('DIV_ExcursiiOptionale_7'),
	('DIV_RecenziiClienti_10');

SELECT * FROM Tests


-- Fac legatira intre teste si tabele
INSERT INTO TestTables (TestID, TableID, NoOfRows, Position)
VALUES
	-- DIV_Clienti_10
	(4, 4, 10, 1),
	-- DIV_ExcursiiOptionale_7
	(5, 5, 7, 2),
	-- DIV_RecenziiClienti_10
	(6, 6, 10, 3);

SELECT * FROM TestTables


-- Fac legatura intre teste si  view-uri
INSERT INTO TestViews
VALUES
	(4, 1),
	(5, 2),
	(6, 3);

SELECT * FROM TestViews


-- Creez procedurile de inserare

-- pentru Clienti
GO
CREATE PROCEDURE ins_test_Clienti
@NoOfRows INT
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @id INT;
	DECLARE @nume varchar(50);
	DECLARE @prenume varchar(50);
	DECLARE @email varchar(100);
	DECLARE @telefon varchar(20);
	DECLARE @last_id INT = (SELECT MAX(Clienti.IDClient) FROM Clienti)
	DECLARE @n INT = 0;
	
	WHILE @N < @NoOfRows
	BEGIN
		SET @id = @last_id + 1;
		SET @nume = 'Nume' + CONVERT(varchar(10), @id);
		SET @prenume = 'Prenume' + CONVERT(varchar(10), @id);
		SET @email = 'email' + CONVERT(varchar(10), @id) + '@example.com';
		SET @telefon = '0712345678';
		INSERT INTO Clienti(IDClient, Nume, Prenume, Email, Telefon)
		VALUES (@id, @nume, @prenume, @email, @telefon);
		SET @last_id = @last_id + 1;
		sET @n = @n +1;
	END

	PRINT 'S-au inserat ' + CONVERT(varchar(10), @NoOfRows) + ' valori in Clienti.'
END

-- pentru ExcursiiOptionale
GO
CREATE PROCEDURE ins_test_ExcursiiOptionale
@NoOfRows INT
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @id INT;
	DECLARE @fk INT = (SELECT TOP 1 IDClient FROM Clienti);
	DECLARE @denumire varchar(50);
	DECLARE @descriere varchar(250);
	DECLARE @pret decimal(10, 2);
	DECLARE @n INT = 0;
	DECLARE @last_id INT = (SELECT MAX(ExcursiiOptionale.IDExcursie) FROM ExcursiiOptionale)

	WHILE @n < @NoOfRows
	BEGIN
		SET @id = @last_id + 1;
		SET @denumire = 'NumeExcursie' + CONVERT(varchar(10), @id);
		SET @descriere = 'Descriere' + CONVERT(varchar(10), @id);
		SET @pret = 40.00 + @id;
		INSERT INTO ExcursiiOptionale(IDExcursie, NumeExcursie, Descriere, Pret, PachetID)
		VALUES (@id, @denumire, @descriere, @pret, @fk)
		SET @last_id = @last_id + 1;
		SET @n = @n + 1;
	END

	PRINT 'S-au inserat ' + CONVERT(varchar(10), @NoOfRows) + ' valori in ExcursiiOptionale.'
END

-- pentru RecenziiClienti
GO
CREATE PROCEDURE ins_test_RecenziiClienti
@NoOfRows INT
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @id_pachet INT = (SELECT TOP 1 PacheteTuristice.IDPachetTuristic FROM PacheteTuristice)
	DECLARE @id_client INT;
	DECLARE @text varchar(max);
	DECLARE @rating INT;
	DECLARE @data DATE;
	DECLARE @n INT = 0;

	DECLARE cursorClient CURSOR FAST_FORWARD FOR
		SELECT Clienti.IDClient FROM Clienti WHERE Clienti.Nume LIKE 'Nume%';

	OPEN cursorClient;

	FETCH NEXT FROM cursorClient INTO @id_client;
	WHILE (@n < @NoOfRows) AND (@@FETCH_STATUS = 0)
	BEGIN
		SET @text = 'TextRecenzie' + CONVERT(varchar(10), @n);
		SET @rating = @n % 6;
		SET @data = CAST(GETDATE() AS DATE);
		INSERT INTO RecenziiClienti(ClientID, PachetID, TextRecenzie, Rating, DataRecenzie)
		VALUES (@id_client, @id_pachet, @text, @rating, @data)
		SET @n = @n + 1;

		FETCH NEXT FROM cursorClient INTO @id_client;
	END

	CLOSE cursorClient;
	DEALLOCATE cursorClient;

	PRINT 'S-au inserat ' + CONVERT(varchar(10), @n) + ' valori in RecenziiClienti.'
END


-- Creez procedurile de stergere
 
-- pentru Clienti
GO
CREATE PROCEDURE del_test_Clienti
AS
BEGIN
	SET NOCOUNT ON;

	DELETE FROM Clienti
	WHERE Clienti.Nume LIKE 'Nume%';
	PRINT 'S-au sters ' + CONVERT(varchar(10), @@ROWCOUNT) + ' valori din Clienti.';
END

-- pentru ExcursiiOptionale
GO
CREATE PROCEDURE del_test_ExcursiiOptionale
AS
BEGIN
	SET NOCOUNT ON;

	DELETE FROM ExcursiiOptionale
	WHERE ExcursiiOptionale.NumeExcursie LIKE 'NumeExcursie%';
	PRINT 'S-au sters ' + CONVERT(varchar(10), @@ROWCOUNT) + ' valori din ExcursiiOptionale.';
END

-- pentru RecenziiClienti
GO
CREATE PROCEDURE del_test_RecenziiClienti
AS
BEGIN
	SET NOCOUNT ON;

	DELETE FROM RecenziiClienti
	WHERE RecenziiClienti.TextRecenzie LIKE 'TextRecenzie%';
	PRINT 'S-au sters ' + CONVERT(varchar(10), @@ROWCOUNT) + ' valori din RecenziiClienti.';
END


-- Creez procedura generala de inserare
GO
CREATE PROCEDURE inserare_test
@idTest INT
AS
BEGIN
	DECLARE @numeTest varchar(50) = (SELECT T.Name FROM Tests T WHERE T.TestID = @idTest);
	DECLARE @numeTabela varchar(50);
	DECLARE @NoOfRows INT;
	DECLARE @procedura varchar(50);

	DECLARE cursorTab CURSOR FORWARD_ONLY FOR
		SELECT Tab.Name, Test.NoOfRows FROM TestTables Test
		INNER JOIN Tables Tab ON Test.TableID = Tab.TableID
		WHERE Test.TestId = @idTest
		ORDER BY Test.Position;
	OPEN cursorTab;

	FETCH NEXT FROM cursorTab INTO @numeTabela, @NoOfRows;
	WHILE (@numeTest NOT LIKE N'DIV_' + @numeTabela + N'_' + CONVERT(varchar(10), @NoOfRows)) AND (@@FETCH_STATUS = 0)
	BEGIN
		SET @procedura = N'ins_test_' + @numeTabela
		EXECUTE	@procedura @NoOfRows;
		FETCH NEXT FROM cursorTab INTO @numeTabela, @NoOfRows;
	END

	SET @procedura = N'ins_test_' + @numeTabela;
	EXECUTE @procedura @NoOfRows;

	CLOSE cursorTab;
	DEALLOCATE cursorTab;
END

EXECUTE inserare_test 4;


-- Creez procedura generala de stergere
GO
CREATE PROCEDURE stergere_test
@idTest INT
AS
BEGIN
	DECLARE @numeTest varchar(50) = (SELECT T.Name FROM Tests T WHERE T.TestID = @idTest);
	DECLARE @numeTabela varchar(50);
	DECLARE @NoOfRows INT;
	DECLARE @procedura varchar(50);

	DECLARE cursorTab CURSOR FORWARD_ONLY FOR
		SELECT Tab.Name, Test.NoOfRows FROM TestTables Test
		INNER JOIN Tables Tab ON Test.TableID = Tab.TableID
		WHERE Test.TestId = @idTest
		ORDER BY Test.Position DESC;
	OPEN cursorTab;

	FETCH NEXT FROM cursorTab INTO @numeTabela, @NoOfRows;
	WHILE (@numeTest NOT LIKE N'DIV_' + @numeTabela + N'_' + CONVERT(varchar(10), @NoOfRows)) AND (@@FETCH_STATUS = 0)
	BEGIN
		SET @procedura = N'del_test_' + @numeTabela
		EXECUTE	@procedura;
		FETCH NEXT FROM cursorTab INTO @numeTabela, @NoOfRows;
	END

	SET @procedura = N'del_test_' + @numeTabela;
	EXECUTE @procedura;

	CLOSE cursorTab;
	DEALLOCATE cursorTab; 
END

EXECUTE stergere_test 4;


-- Creez procedura generala pentru view-uri
GO
CREATE PROCEDURE view_test
@idTest INT
AS
BEGIN
	DECLARE @viewName varchar(50) = 
		(SELECT V.Name FROM Views V
		INNER JOIN TestViews TV ON TV.ViewID = V.ViewID
		WHERE TV.TestID = @idTest);

	DECLARE @comanda varchar(55) = N'SELECT * FROM ' + @viewName;

	EXECUTE (@comanda);
END

EXECUTE view_test 1;


-- Creez prodecura de rulare a unui test
GO
CREATE OR ALTER PROCEDURE run_test
@idTest INT
AS
BEGIN
	DECLARE @startTime DATETIME;
	DECLARE @interTime DATETIME;
	DECLARE @endTime DATETIME;

	SET @startTime = GETDATE();

	EXECUTE stergere_test @idTest;
	EXECUTE inserare_test @idTest;

	SET @interTime = GETDATE();

	EXECUTE view_test @idTest;

	SET @endTime = GETDATE();

	DECLARE @testName varchar(50) = 
		(SELECT T.Name FROM Tests T WHERE T.TestID = @idTest);
	INSERT INTO TestRuns VALUES (@testName, @startTime, @endTime);

	DECLARE @viewID INT = 
		(SELECT V.ViewID FROM Views V
		INNER JOIN TestViews TV ON TV.ViewID = V.ViewID
		WHERE TV.TestID = @idTest);
	DECLARE @tableID INT = 
		(SELECT TB.TableID FROM Tests T
		INNER JOIN TestTables TT ON T.TestID = TT.TestID
		INNER JOIN Tables TB ON TB.TableID = TT.TableID
		WHERE T.TestID = @idTest AND
		T.Name LIKE N'DIV_' + TB.Name + N'_' + CONVERT(varchar(10), TT.NoOfRows));
	DECLARE @testRunID INT = 
		(SELECT TOP 1 T.TestRunID FROM TestRuns T
		WHERE T.Description = @testName
		ORDER BY T.TestRunID DESC);

	INSERT INTO TestRunTables VALUES (@testRunID, @tableID, @startTime, @interTime);
	INSERT INTO TestRunViews VALUES (@testRunID, @viewID, @interTime, @endTime);

	PRINT CHAR(10) + 'TEST COMPLETAT CU SUCCES IN ' + CONVERT(varchar(10), DATEDIFF(millisecond, @startTime, @endTime)) + ' MILISECUNDE.'
END

EXECUTE run_test 6;
GO

SELECT * FROM Clienti
SELECT * FROM ExcursiiOptionale
SELECT * FROM RecenziiClienti

SELECT * FROM Tables
SELECT * FROM TestRuns
SELECT * FROM TestRunTables
SELECT * FROM TestRunViews
SELECT * FROM Tests
SELECT * FROM TestTables
SELECT * FROM TestViews
SELECT * FROM Views


DELETE FROM TestRuns