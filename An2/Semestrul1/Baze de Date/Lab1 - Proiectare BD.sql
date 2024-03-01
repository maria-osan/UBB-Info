Create database Calatorii
go
use Calatorii;
go

CREATE TABLE Clienti (
	IDClient INT PRIMARY KEY,
	Nume varchar(50),
	Prenume varchar(50),
	Email varchar(100),
	Telefon varchar(20)
)

CREATE TABLE Destinatii (
	IDDestinatie INT PRIMARY KEY,
	NumeDestinatie varchar(50),
	Descriere varchar(250),
	Tara varchar(50),
	Oras varchar(50)
)

CREATE TABLE PacheteTuristice (
	IDPachetTuristic INT PRIMARY KEY,
	NumePachet varchar(50),
	Descriere varchar(250),
	Pret decimal(10, 2),
	DestinatieID INT FOREIGN KEY REFERENCES Destinatii(IDDestinatie)
)


CREATE TABLE Rezervari (
	IDRezervare INT PRIMARY KEY,
	DataInceput date,
	DataSfarsit date,
	ClientID INT FOREIGN KEY REFERENCES Clienti(IDClient),
	PachetID INT FOREIGN KEY REFERENCES PacheteTuristice(IDPachetTuristic)
)

CREATE TABLE Transporturi (
	IDTransport INT PRIMARY KEY,
	TipTransport varchar(50),
	CompanieTransport varchar(50),
	PretBilet decimal(10, 2),
	PachetID INT FOREIGN KEY REFERENCES PacheteTuristice(IDPachetTuristic)
)

CREATE TABLE Hoteluri (
	IDHotel INT PRIMARY KEY,
	NumeHotel varchar(50),
	Stele int,
	Adresa varchar(100),
	PretCamera decimal(10, 2),
	PachetID INT FOREIGN KEY REFERENCES PacheteTuristice(IDPachetTuristic)
)

CREATE TABLE CamereHotel (
	IDCameraHotel INT PRIMARY KEY,
	TipCamera varchar(50),
	Capacitate int,
	PretNoapte decimal(10, 2),
	HotelID INT FOREIGN KEY REFERENCES Hoteluri(IDHotel)
)

CREATE TABLE Plati (
	IDPlata INT PRIMARY KEY,
	SumaPlata decimal(10, 2),
	DataPlata date,
	MetodaPlata varchar(50),
	RezervareID INT FOREIGN KEY REFERENCES Rezervari(IDRezervare)
)

CREATE TABLE ExcursiiOptionale (
	IDExcursie INT PRIMARY KEY,
	NumeExcursie varchar(50),
	Descriere varchar(250),
	Pret decimal(10, 2),
	PachetID INT FOREIGN KEY REFERENCES PacheteTuristice(IDPachetTuristic)
)

CREATE TABLE RecenziiClienti (
	ClientID INT FOREIGN KEY REFERENCES Clienti(IDClient),
	PachetID INT FOREIGN KEY REFERENCES PacheteTuristice(IDPachetTuristic),
	CONSTRAINT IDRecenzie PRIMARY KEY (ClientID, PachetID),
	TextRecenzie varchar(max),
	Rating int,
	DataRecenzie date,
)