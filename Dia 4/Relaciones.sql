create table vacunaciones(
	id int primary key auto_increment,
    nombre varchar(50) unique not null,
    estado bool default true,
    fecha_vencimiento date,
    procedencia ENUM('USA','CHINA','RUSIA','UK'),
    lote varchar(10)
);

rename table vacunaciones to vacunas;

create table vacunatorio(
	id int primary key auto_increment,
    nombre varchar(100) not null,
    latitud float,
    longitud float,
    direccion varchar(200),
    horario_atencion varchar(100),
    -- SE CREARA CLAVE FORANEA
    vacuna_id int,
    foreign key(vacuna_id) references vacunas(id)
);

rename table vacunatorio to vacunatorios;

#alter table vacunatorios drop column latitud;
alter table vacunatorios add column imagen varchar(100) default 'imagen.png' after horario_atencion;

-- modificar nombre de columna
alter table vacunatorios rename column imagen to foto;

-- modificar columna tipo dato, etc si, la columna esta vacia o info que no genere error
-- segun propeidad que estoy agregando
-- alter table vacunatorios modify column imagen  char(100) unique not null;

-- para saber todo los detalles de la tabla
desc clientes;

