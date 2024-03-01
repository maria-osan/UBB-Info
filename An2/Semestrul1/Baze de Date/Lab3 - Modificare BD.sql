-- modifica tipul unei coloane
CREATE PROCEDURE ChangeDestinatii_Descriere_to_nvarchar
AS
BEGIN
	ALTER TABLE Destinatii
	ALTER COLUMN Descriere nvarchar(250);
	print 's-a modificat tipul coloanei...'
END
GO

CREATE PROCEDURE ChangeDestinatii_Descriere_to_varchar
AS
BEGIN
	ALTER TABLE Destinatii
	ALTER COLUMN Descriere varchar(250);
	print 's-a modificat tipul coloanei...'
END
GO

EXEC ChangeDestinatii_Descriere_to_nvarchar;
EXEC ChangeDestinatii_Descriere_to_varchar;
GO


-- adauga o constrangere de "valoare implicita" pentru un camp
-- adds default value to DataPlata
CREATE PROCEDURE Add_Default_Value_Plati_DataPlata
AS
BEGIN
	ALTER TABLE Plati
	ADD CONSTRAINT DF_DataPlata
	DEFAULT GETDATE() FOR DataPlata;
	print 's-a adaugat constrangerea...'
END
GO

CREATE PROCEDURE Delete_Default_Value_Plati_DataPlata
AS
BEGIN
	ALTER TABLE Plati
	DROP CONSTRAINT DF_DataPlata; /* sau ALTER COLUMN DataPlata DROP DEFAULT; */
	print 's-a sters constrangerea...'
END
GO

EXEC Add_Default_Value_Plati_DataPlata;
EXEC Delete_Default_Value_Plati_DataPlata;
GO


-- creeaza / sterge o tabela
CREATE PROCEDURE Creeaza_Tabela_Activitati
AS
BEGIN
	CREATE TABLE Activitati (
	IDActivitate INT NOT NULL PRIMARY KEY,
	NumeActivitate varchar(50),
	Descriere varchar(250),
	DataActivitate date,
	Locatie varchar(100),
	Pret decimal(10, 2),
	PachetID int
	);
	print 's-a creeat tabela...'
END
GO

CREATE PROCEDURE Sterge_Tabela_Activitati
AS
BEGIN
	DROP TABLE Activitati;
	print 's-a sters tabela...'
END
GO

EXEC Creeaza_Tabela_Activitati;
EXEC Sterge_Tabela_Activitati;
GO


-- adauga / sterge un camp nou
CREATE PROCEDURE Adauga_Camp_Nou
AS
BEGIN
	ALTER TABLE Clienti
	ADD Adresa varchar(100);
	print 's-a adaugat coloana...'
END
GO

CREATE PROCEDURE Sterge_Camp_Nou
AS
BEGIN
	ALTER TABLE Clienti
	DROP COLUMN Adresa;
	print 's-a sters coloana...'
END
GO

EXEC Adauga_Camp_Nou;
EXEC Sterge_Camp_Nou;
GO


-- creeaza / sterge constrangere de cheie straina
CREATE PROCEDURE Creeaza_Cheie_Straina
AS
BEGIN
	ALTER TABLE Activitati
	ADD CONSTRAINT FK_PachetID 
	FOREIGN KEY (PachetID) REFERENCES PacheteTuristice(IDPachetTuristic);
	print 's-a creeat constrangerea de cheie straina...'
END
GO

CREATE PROCEDURE Sterge_Cheie_Straina
AS
BEGIN
	ALTER TABLE Activitai
	DROP CONSTRAINT FK_PachetID;
	print 's-a sters constrangerea de cheie straina...'
END
GO

EXEC Creeaza_Cheie_Straina;
EXEC Sterge_Cheie_Straina;
GO


-- cream tabelul cu versiunea bazei de date
CREATE TABLE VersiuneBD (
	NumarVersiune INT DEFAULT 0
);

INSERT INTO VersiuneBD
VALUES (0);

SELECT * FROM VersiuneBD;


-- cream doua tabele auxiliare
CREATE TABLE ListaProceduriVersiuniBD (
	ID INT PRIMARY KEY,
	NumeProcedura varchar(100)
);

INSERT INTO ListaProceduriVersiuniBD
VALUES
(0, 'ChangeDestinatii_Descriere_to_nvarchar'),
(1, 'Add_Default_Value_Plati_DataPlata'),
(2, 'Creeaza_Tabela_Activitati'),
(3, 'Adauga_Camp_Nou'),
(4, 'Creeaza_Cheie_Straina');

CREATE TABLE ListaOpusProceduriVersiuniBD (
	ID INT PRIMARY KEY,
	NumeProcedura varchar(100)
);

INSERT INTO ListaOpusProceduriVersiuniBD
VALUES
(1, 'ChangeDestinatii_Descriere_to_varchar'),
(2, 'Delete_Default_Value_Plati_DataPlata'),
(3, 'Sterge_Tabela_Activitati'),
(4, 'Sterge_Camp_Nou'),
(5, 'Sterge_Cheie_Straina');

SELECT * FROM ListaProceduriVersiuniBD;
SELECT * FROM ListaOpusProceduriVersiuniBD;
GO


-- main stored procedure
CREATE PROCEDURE main
@vers int
AS
BEGIN
	IF @vers > 5
	BEGIN
		RAISERROR('nu exista decat 6 veriuni ale bazei de date (de la 0 la 5 inclusiv)', 16, 1);
		RETURN;
	END

	DECLARE @vers_actuala AS INT
	SELECT @vers_actuala = NumarVersiune
	FROM VersiuneBD;

	PRINT 'versiunea actuala este: '
	PRINT @vers_actuala
	PRINT 'schimbam la versiunea: '
	PRINT @vers

	IF @vers = @vers_actuala
	BEGIN
		PRINT 'suntem deja in aceasta veriune'
		RETURN;
	END

	DECLARE @procedure AS varchar(100);

	IF @vers > @vers_actuala
	BEGIN
		WHILE @vers != @vers_actuala
		BEGIN
			SELECT @procedure = NumeProcedura
			FROM ListaProceduriVersiuniBD
			WHERE @vers_actuala = ID;

			EXECUTE @procedure;

			SET @vers_actuala = @vers_actuala + 1;
		END

		UPDATE VersiuneBD
		SET NumarVersiune = @vers;

		RETURN;
	END

	-- altfel daca @vers < @vers_actuala

	WHILE @vers != @vers_actuala
	BEGIN
		SELECT @procedure = NumeProcedura
		FROM ListaOpusProceduriVersiuniBD
		WHERE @vers_actuala = ID;

		EXECUTE @procedure

		SET @vers_actuala = @vers_actuala - 1;
	END

	UPDATE VersiuneBD
	SET NumarVersiune = @vers;
	RETURN;
END
GO

EXEC main 4
EXEC main 2
EXEC main 7
EXEC main 0

DROP PROCEDURE main

UPDATE VersiuneBD
SET NumarVersiune = 0;