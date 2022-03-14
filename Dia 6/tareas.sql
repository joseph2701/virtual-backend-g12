use colegios;
-- 1. Todos los alumnos que tienen correo GMAIL
select * from alumnos where correo like '%@gmail%';

-- 2. Todos los alumnos (nombre, ap_pat, ap_mat) que hayan cursado en el 2002
select a.nombre,a.apellido_paterno,a.apellido_materno from alumnos a
inner join alumnos_niveles an on a.id=an.alumnos_id
where an.fecha_cursada=2002;

-- 3. Todos los grados donde su ubicacion sea el sotano o segundo piso
select * from niveles where ubicacion like 'Sotano' or ubicacion like 'Segundo Piso';

-- 4. Todos los grados (Seccion y el nombre ) que han tenido alumnos en el año 2003
select n.seccion,n.nombre from niveles n 
inner join alumnos_niveles an on n.id=an.nivel_id
where an.fecha_cursada=2003;

-- 5. Mostrar todos los alumnos del quinto A
select distinct a.*
from alumnos a
inner join alumnos_niveles an on a.id=an.alumnos_id
inner join niveles n on an.nivel_id=n.id
where n.nombre='Quinto' and n.seccion='A';

-- 6. Mostrar todos los correos de los alumnos del primero B 
select distinct a.correo
from alumnos a
left join alumnos_niveles an on a.id=an.alumnos_id
left join niveles n on an.nivel_id=n.id
where n.nombre='Primero' and n.seccion='B';

-- -----------------------------------------------------------------------------
-- select * from alumnos;
-- select * from niveles;

-- select an.id,an.alumnos_id,a.nombre,an.nivel_id,n.nombre,an.fecha_cursada from alumnos_niveles an
-- inner join alumnos a on a.id=an.alumnos_id
-- inner join niveles n on n.id=an.nivel_id;


