--- Verifica daca un string este null sau gol
CREATE OR ALTER FUNCTION dbo.isValidText (@text varchar(100))
RETURNS BIT
AS
BEGIN
	DECLARE @isValid BIT

	IF @text IS NOT NULL AND LEN(LTRIM(RTRIM(@text))) > 0
		SET @isValid = 1
	ELSE
		SET @isValid = 0

	RETURN @isValid
END
GO

--- Verifica daca adresa de email este valida
CREATE OR ALTER FUNCTION dbo.isValidEmail (@email varchar(100))
RETURNS BIT
AS
BEGIN
	DECLARE @isValid BIT

	IF @email LIKE '%[a-zA-Z0-9._]%@[a-zA-Z0-9.-]%.[a-zA-Z]%'
		SET @isValid = 1
	ELSE
		SET @isValid = 0

	RETURN @isValid
END
GO

--- Verifica daca numarul de telefon este valid
CREATE OR ALTER FUNCTION dbo.isValidPhoneNumber (@phoneNumber varchar(20))
RETURNS BIT
AS
BEGIN
	DECLARE @isValid BIT

	IF @phoneNumber LIKE '%07[0-9]%' AND LEN(@phoneNumber) = 10
		SET @isValid = 1
	ELSE
		SET @isValid = 0

	RETURN @isValid
END
GO

--- Verifica daca pretul este valid
CREATE OR ALTER FUNCTION dbo.isValidPrice (@price DECIMAL(10, 2))
RETURNS BIT
AS
BEGIN
	DECLARE @isValid BIT

	IF @price >= 0 AND @price <= 1000000 AND @price = ROUND(@price, 2)
		SET @isValid = 1
	ELSE
		SET @isValid = 0

	RETURN @isValid
END
GO

--- Verifica daca rating-ul este valid
CREATE OR ALTER FUNCTION dbo.isValidRating (@rating DECIMAL(5, 2))
RETURNS BIT
AS
BEGIN
	DECLARE @isValid BIT

	IF @rating >=0 AND @rating <= 5 AND (@rating = ROUND(@rating, 0) OR @rating = ROUND(@rating, 2))
		SET @isValid = 1
	ELSE
		SET @isValid = 0

	RETURN @isValid
END
GO



---- Cerinta 1 ----
CREATE OR ALTER PROCEDURE AddRecenzie
	--- Client
	@nume varchar(100), @prenume varchar(100), @email varchar(100), @telefon varchar(20),
	--- Pachet turistic
	@nume_pachet varchar(100), @descriere varchar(100), @pret decimal(10, 2),
	--- Rating
	@text_recenzie varchar(max), @rating decimal(5, 2), @data_recenzie date
AS
BEGIN
BEGIN TRAN
	BEGIN TRY
		DECLARE @err varchar(100) = ''
		
		-- validare client
		IF dbo.isValidText(@nume) <> 1
		BEGIN
			PRINT 'Nume invalid'
			SET @err += 'Nume invalid; '
		END
		IF dbo.isValidText(@prenume) <> 1
		BEGIN
			PRINT 'Prenume invalid'
			SET @err += 'Prenume invalid; '
		END
		IF dbo.isValidEmail(@email) <> 1
		BEGIN
			PRINT 'Email invalid'
			SET @err += 'Email invalid; '
		END
		IF dbo.isValidPhoneNumber(@telefon) <> 1
		BEGIN
			PRINT 'Telefon invalid'
			SET @err += 'Telefon invalid; '
		END

		-- validare pachet
		IF dbo.isValidText(@nume_pachet) <> 1
		BEGIN
			PRINT 'Nume pachet invalid'
			SET @err += 'Nume pachet invalid; '
		END
		IF dbo.isValidText(@descriere) <> 1
		BEGIN
			PRINT 'Descriere pachet invalida'
			SET @err += 'Descriere pachet invalida; '
		END
		IF dbo.isValidPrice(@pret) <> 1
		BEGIN
			PRINT 'Pret invalid'
			SET @err += 'Pret invalid; '
		END

		-- validare rating
		IF dbo.isValidText(@text_recenzie) <> 1
		BEGIN
			PRINT 'Text recenzie invalid'
			SET @err += 'Text recenzie invalid; '
		END
		IF dbo.isValidRating(@rating) <> 1
		BEGIN
			PRINT 'Rating invalid'
			SET @err += 'Rating invalid; '
		END

		IF @err <> ''
		BEGIN
			RAISERROR(@err, 14, 1)
		END

		-- inserate client
		DECLARE @client_id INT
		SET @client_id = (SELECT MAX(Clienti.IDClient) FROM Clienti) + 1

		INSERT INTO Clienti (IDClient, Nume, Prenume, Email, Telefon)
		VALUES (@client_id, @nume, @prenume, @email, @telefon)

		PRINT 'Client adaugat'

		-- incerare pachet
		DECLARE @pachet_id INT
		SET @pachet_id = (SELECT MAX(PacheteTuristice.IDPachetTuristic) FROM PacheteTuristice) + 1

		DECLARE @randomID INT
		SELECT TOP 1 @randomID = IDDestinatie
		FROM Destinatii
		ORDER BY NEWID();

		INSERT INTO PacheteTuristice (IDPachetTuristic, NumePachet, Descriere, Pret, DestinatieID)
		VALUES (@pachet_id, @nume_pachet, @descriere, @pret, @randomID)

		PRINT 'Pachet turistic adaugat'

		-- inserare recenzie
		INSERT INTO RecenziiClienti (ClientID, PachetID, TextRecenzie, Rating, DataRecenzie)
		VALUES (@client_id, @pachet_id, @text_recenzie, @rating, @data_recenzie)

		PRINT 'Recenzie adaugata'

		COMMIT TRAN
		SELECT 'Transaction commited'
	END TRY

	BEGIN CATCH
		ROLLBACK TRAN
		PRINT ERROR_MESSAGE();
		SELECT 'Transaction rollback'
	END CATCH
END
GO


SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie 'Nume', 'Prenume', 'nume@email.com', '0787654321', 'Nume pachet', 'descriere', 1449.99,
		'text recenzie', 4.3, '2024-04-16'
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti

-- nume, telefon, descriere invalide
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie '', 'Prenume', 'nume@email.com', '0271234567', 'Nume pachet', '', 390,
		'text recenzie', 4, '2024-04-16'
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti

-- email, telefon, rating invalide
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie 'Nume', 'Prenume', 'numeemail.com', '0712345', 'Nume pachet', 'descriere', 390,
		'text recenzie', -1, '2024-04-16'
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti

-- pret, text recenzie, rating invalide
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie 'Nume', 'Prenume', 'nume@email.com', '0712345678', 'Nume pachet', 'descriere', -12.5,
		'', 6, '2024-04-16'
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
GO



---- Cerinta 2 ----
-- inserare client
CREATE OR ALTER PROCEDURE AddClient
	@nume varchar(100), @prenume varchar(100), @email varchar(100), @telefon varchar(20)
AS
BEGIN
	BEGIN TRAN

	BEGIN TRY
		DECLARE @err varchar(100) = ''
		
		-- validare nume
		IF dbo.isValidText(@nume) <> 1
		BEGIN
			PRINT 'Nume invalid'
			SET @err += 'Nume invalid; '
		END
		-- validare prenume
		IF dbo.isValidText(@prenume) <> 1
		BEGIN
			PRINT 'Prenume invalid'
			SET @err += 'Prenume invalid; '
		END
		-- validare email
		IF dbo.isValidEmail(@email) <> 1
		BEGIN
			PRINT 'Email invalid'
			SET @err += 'Email invalid; '
		END
		-- validare telefon
		IF dbo.isValidPhoneNumber(@telefon) <> 1
		BEGIN
			PRINT 'Telefon invalid'
			SET @err += 'Telefon invalid; '
		END

		IF @err <> ''
		BEGIN
			RAISERROR(@err, 14, 1)
		END

		-- inserate client
		DECLARE @client_id INT
		SET @client_id = (SELECT MAX(Clienti.IDClient) FROM Clienti) + 1

		INSERT INTO Clienti (IDClient, Nume, Prenume, Email, Telefon)
		VALUES (@client_id, @nume, @prenume, @email, @telefon)

		PRINT 'Client adaugat'

		COMMIT TRAN
		SELECT 'Transaction commited'
	END TRY

	BEGIN CATCH
		ROLLBACK TRAN
		PRINT ERROR_MESSAGE();
		SELECT 'Transaction rollback'
		RETURN 0
	END CATCH

	RETURN 1
END
GO

-- inserare pachet
CREATE OR ALTER PROCEDURE AddPachet
	@nume_pachet varchar(100), @descriere varchar(100), @pret decimal(10, 2)
AS
BEGIN
	BEGIN TRAN

	BEGIN TRY
		DECLARE @err varchar(100) = ''

		-- validare nume pachet
		IF dbo.isValidText(@nume_pachet) <> 1
		BEGIN
			PRINT 'Nume pachet invalid'
			SET @err += 'Nume pachet invalid; '
		END
		-- validare descriere
		IF dbo.isValidText(@descriere) <> 1
		BEGIN
			PRINT 'Descriere pachet invalida'
			SET @err += 'Descriere pachet invalida; '
		END
		-- validare pret
		IF dbo.isValidPrice(@pret) <> 1
		BEGIN
			PRINT 'Pret invalid'
			SET @err += 'Pret invalid; '
		END

		IF @err <> ''
		BEGIN
			RAISERROR(@err, 14, 1)
		END

		-- inserare pachet
		DECLARE @pachet_id INT
		SET @pachet_id = (SELECT MAX(PacheteTuristice.IDPachetTuristic) FROM PacheteTuristice) + 1

		DECLARE @randomID INT
		SELECT TOP 1 @randomID = IDDestinatie
		FROM Destinatii
		ORDER BY NEWID();

		INSERT INTO PacheteTuristice (IDPachetTuristic, NumePachet, Descriere, Pret, DestinatieID)
		VALUES (@pachet_id, @nume_pachet, @descriere, @pret, @randomID)

		PRINT 'Pachet turistic adaugat'

		COMMIT TRAN
		SELECT 'Transaction commited'
	END TRY

	BEGIN CATCH
		ROLLBACK TRAN
		PRINT ERROR_MESSAGE();
		SELECT 'Transaction rollback'
		RETURN 0
	END CATCH

	RETURN 1
END
GO


-- inserare recenzie
CREATE OR ALTER PROCEDURE AddRecenzie2
	--- Client
	@nume varchar(100), @prenume varchar(100), @email varchar(100), @telefon varchar(20),
	--- Pachet turistic
	@nume_pachet varchar(100), @descriere varchar(100), @pret decimal(10, 2)
AS
BEGIN
	DECLARE @addClient int
	DECLARE @addPachet int

	EXEC @addClient = AddClient @nume, @prenume, @email, @telefon
	EXEC @addPachet = AddPachet  @nume_pachet, @descriere, @pret

	IF @addClient <> 1
	BEGIN
		PRINT 'Clientul nu s-a adaugat deci nu putem adauga recenzia'
		RETURN 0
	END

	IF @addPachet <> 1
	BEGIN
		PRINT 'Pachetul turistic nu s-a adaugat deci nu putem adauga recenzia'
		RETURN 0
	END

	DECLARE @client_id int
	DECLARE @pachet_id int

	SELECT TOP 1 @client_id = IDClient
	FROM Clienti AS C
	WHERE C.Email = @email
	ORDER BY IDClient DESC

	SELECT TOP 1 @pachet_id = IDPachetTuristic
	FROM PacheteTuristice AS PT
	WHERE PT.NumePachet = @nume_pachet
	ORDER BY IDPachetTuristic DESC

	INSERT INTO RecenziiClienti (ClientID, PachetID, TextRecenzie, Rating, DataRecenzie)
	VALUES (@client_id, @pachet_id, 'text recenzie', 4.3,  CAST(GETDATE() AS DATE))

	PRINT 'Recenzie adaugata'
END
GO


SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie2 'Nume', 'Prenume', 'nume_cerinta2@email.com', '0712345678', 'Nume pachet cerinta 2', 'descriere', 1449.99
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti

-- nume, telefon invalide
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie2 '', 'Prenume', 'nume_cerinta2@email.com', '0271234567', 'Nume pachet cerinta 2', 'descriere', 39.90
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti

-- descriere, pret invalide
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie2 'Nume', 'Prenume', 'nume_cerinta2@email.com', '0787654321', 'Nume pachet cerinta 2', '', -14.99
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti

-- email, nume pachet invalide
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti
EXEC AddRecenzie2 'Nume', 'Prenume', 'nume_cerinta2email.com', '0712345678', '', 'descriere', 1449.99
SELECT * FROM Clienti
SELECT * FROM PacheteTuristice
SELECT * FROM RecenziiClienti