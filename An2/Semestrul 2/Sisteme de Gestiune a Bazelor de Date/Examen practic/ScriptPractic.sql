create database S13
go
use S13
go
-- drop database S13


create table Muzee(
Mid int primary key identity,
Denumire varchar(50),
TipMuzeu varchar(50),
AnDeschidere int,
NrExponate int)

create table Expozitii(
Eid int primary key identity,
Denumire varchar(50),
Descriere varchar(50),
DataIncepere date,
DataInchidere date,
Mid int foreign key references Muzee(Mid))

create table TipuriTablouri(
Tid int primary key identity,
Tip varchar(50),
Descriere varchar(50),
MrMediuTablouri int)

create table Tablouri(
TabId int primary key identity,
Denumire varchar(50),
AnPictura int,
Dimensiune varchar(30),
Perioada varchar(50),
Tid int foreign key references TipuriTablouri(Tid))

create table Tari(
TaId int primary key identity,
Denumire varchar(50),
Stat varchar(50),
Continent varchar(50))

create table Expuneri(
Eid int foreign key references Expozitii(Eid),
Tid int foreign key references TipuriTablouri(Tid),
NrExponate int,
constraint pk_Expuneri primary key(Eid, Tid))

-- 1-n: Muzee-Expozitii

select * from Muzee
select * from Expozitii
select * from TipuriTablouri
select * from Tablouri
select * from Expuneri


insert into Muzee values('Van Gog', 'muzeu cu picturi', 1958, 250),
('Bruckental', 'muzeu cu picturi si sculpturi', 1990, 127)

insert into Expozitii values
('Vara pe ulite', 'vara in diverse locatii', '12/05/2023', '12/09/2023', 1),
('Zburand cu libelulele', 'zbor lin pe campuri', '06/06/2023', '07/07/2023', 2)

insert into TipuriTablouri values 
('tablouri cu peisaje', 'peisaje de munte, deal, campii', 50),
('tablouri cu animale', 'animale din toate mediile', 20)

insert into Tablouri values('Fresca de vara', 1946, '40*60', 'Renascentista', 1), 
('Abstract de seara', 1867, '30*20', 'Gotic', 2)

insert into Expuneri values(1, 1, 49), (1, 2, 27)

