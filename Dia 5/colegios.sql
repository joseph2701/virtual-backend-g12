create database colegios;
use colegios;
create table if not exists alumnos(
	id int primary key auto_increment,
    nombre varchar(45) not null,
    apellido_paterno varchar(45),
    apellido_materno varchar(45),
    correo varchar(45) unique,
    numero_emergencia varchar(45) not null
);
create table if not exists niveles(
	id int primary key auto_increment,
    seccion varchar(45) not null,
    ubicacion varchar(45),
    nombre varchar(45) not null unique
);
create table if not exists alumnos_niveles(
	id int primary key auto_increment,
    fecha_cursada varchar(45),
    alumnos_id int not null,
    nivel_id int not null,
    foreign key(alumnos_id) references alumnos(id),
    foreign key(nivel_id) references niveles(id)
);
use colegios;
select * from alumnos_niveles;