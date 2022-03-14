
#---------------------------------------------------
insert into clientes(nombre,documento,tipo_documento,estado)
values('Eduardo','73500746','DNI',true);
insert into clientes(nombre,documento,tipo_documento,estado)
values	('Estefani','12345766','DNI',true),
		('Juan','23461239','RUC',true);
select * from clientes;
select * from clientes where estado=1;
select * from clientes where estado=true;
select * from clientes where nombre like '%duardo%';
select * from clientes where tipo_documento='DNI' and estado=True;
update clientes set nombre='Ramiro' where documento='12345766'and estado=1;
-- desactivamos modo seguro del servidor
set sql_Safe_updates=false;

#---------------------------------------------------