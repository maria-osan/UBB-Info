CREATE DATABASE Gestionare1Filme
GO
USE Gestionare1Filme
GO


----- CREARE TABELE -----
CREATE TABLE TipuriFilme (
	id INT PRIMARY KEY IDENTITY,
	denumire VARCHAR(50) NOT NULL,
	descriere VARCHAR(250) NOT NULL
);

CREATE TABLE Platouri (
	id INT PRIMARY KEY IDENTITY,
	nume VARCHAR(50) NOT NULL,
	strada VARCHAR(100) NOT NULL,
	numar INT NOT NULL,
	localitate VARCHAR(50) NOT NULL
);

CREATE TABLE Filme (
	id INT PRIMARY KEY IDENTITY,
	denumire VARCHAR(50) NOT NULL,
	durata INT NOT NULL,
	platou_id INT FOREIGN KEY REFERENCES Platouri(id),
	tip_id INT FOREIGN KEY REFERENCES TipuriFilme(id)
);

CREATE TABLE Regizori (
	id INT PRIMARY KEY IDENTITY,
	nume VARCHAR(50) NOT NULL,
	prenume VARCHAR(50) NOT NULL,
	gen VARCHAR(20) NOT NULL,
	varsta INT NOT NULL
);

CREATE TABLE RegizoriPlatouri (
	regizor_id INT FOREIGN KEY REFERENCES Regizori(id),
	platou_id INT FOREIGN KEY REFERENCES Platouri(id),
	data_inceput DATE NOT NULL,
	data_final DATE NOT NULL,
	CONSTRAINT pk_regizori_platouri PRIMARY KEY (regizor_id, platou_id)
 );


 ----- INSERARI -----
 INSERT INTO TipuriFilme (denumire, descriere)
 VALUES
 ('Denumire1', 'descriere1'),
 ('Denumire2', 'descriere2'),
 ('Denumire3', 'descriere3');

 INSERT INTO Platouri (nume, strada, numar, localitate)
 VALUES
 ('Nume1', 'strada1', 1, 'Localitate1'),
 ('Nume2', 'strada2', 2, 'Localitate2'),
 ('Nume3', 'strada3', 3, 'Localitate3');

 INSERT INTO Filme (denumire, durata, platou_id, tip_id)
 VALUES
 ('Denumire1', 120, 1, 1),
 ('Denumire2', 90, 2, 2),
 ('Denumire3', 135, 3, 3),
 ('Denumire4', 100, 1, 2);

INSERT INTO Regizori (nume, prenume, gen, varsta)
VALUES
('Nume1', 'Prenume1', 'm', 35),
('Nume2', 'Prenume2', 'f', 40),
('Nume3', 'Prenume3', 'm', 47);

INSERT INTO RegizoriPlatouri (regizor_id, platou_id, data_inceput, data_final)
VALUES
(1, 1, '2021-01-01', '2022-01-01'),
(2, 2, '2022-02-20', '2022-12-02'),
(3, 3, '2023-03-03', '2023-03-13');

SELECT * FROM TipuriFilme
SELECT * FROM Platouri
SELECT * FROM Filme
SELECT * FROM Regizori
SELECT * FROM RegizoriPlatouri
GO


----- PRODECURA STOCATA -----
CREATE OR ALTER PROCEDURE adauga
	@id_regizor INT,
	@id_platou INT,
	@data_inceput DATE,
	@data_final DATE
AS
BEGIN
	IF(EXISTS(SELECT * FROM RegizoriPlatouri WHERE @id_regizor = regizor_id AND @id_platou = platou_id))
	BEGIN
		UPDATE RegizoriPlatouri
		SET data_inceput = @data_inceput, data_final = @data_final
		WHERE @id_regizor = regizor_id AND @id_platou = platou_id;
	END

	ELSE
	BEGIN
		INSERT INTO RegizoriPlatouri (regizor_id, platou_id, data_inceput, data_final)
		VALUES (@id_regizor, @id_platou, @data_inceput, @data_final);
	END
END
GO

EXEC adauga 1, 2, '2021-12-21', '2022-01-20'
EXEC adauga 1, 2, '2022-01-12', '2022-02-21'

SELECT * FROM RegizoriPlatouri
GO

----- FUNCTIA -----
CREATE OR ALTER FUNCTION afisarePlatouri (
	@n INT
)
RETURNS TABLE AS
RETURN
	SELECT P.nume, COUNT(*) AS Numar_filme
	FROM Platouri P
	INNER JOIN Filme F ON F.platou_id = P.id
	GROUP BY P.nume
	HAVING COUNT(*) >= @n

GO

SELECT * FROM dbo.afisarePlatouri(2)