create table users (
	id serial primary key,
	name varchar(100),
	email varchar(100),
	username varchar(100),
	password varchar(100),
	isAdmin boolean
);

select * from users;

create table seats (
	id serial primary key,
	nr varchar(10),
	seatRow int,
	seatColumn int,
	price real,
	isAvailable boolean
);

select * from seats;

create table movies (
	id serial primary key,
	name varchar(100),
	genre varchar(50),
	movieDate date,
	movieTime time
);

select * from movies;

create table tickets (
	id serial primary key,
	buyerName varchar(100),
	price real,
	movieId bigint,
	seats varchar(255),
	foreign key (movieId) references movies(id) on delete cascade
);

select * from tickets;