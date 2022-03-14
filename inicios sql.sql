create Database prueba;

use prueba;
create table clientes(	
id int auto_increment primary key,
#text > espacio dinamico segun sea necesario, no tiene limite
nombre VARCHAR(500) not null,
documento VARCHAR(8) UNIQUE,
tipo_documento ENUM('C.E.','DNI','RUC','PASAPORTE','C.M.','OTRO'),
estado BOOL
);

