use prueba;
insert into vacunas(nombre,estado,fecha_vencimiento,procedencia,lote)
values 		('PFIZER', true, '2022-08-16', 'USA', '123jkl'),
			('SINOPHARM', true, '2022-10-10', 'CHINA', 'vxcvxc'),
			('MODERNA', true, '2022-09-14', 'USA', 'zxczxc'),
			('SPUTNIK', false, '2022-10-04', 'RUSIA', 'ghjkhjfg');
        
-- ---------------------------------------------------------
select nombre from vacunas;
select * from vacunas where procedencia like 'USA';
select * from vacunas where procedencia not like 'USA';
select * from vacunas where lote like '%xc%';
-- ---------------------------------------------------------
select * from vacunatorios where horario_atencion like '%MIE%' or horario_atencion like 'LUN-JUE' or horario_atencion like 'LUN-VIE'or horario_atencion like 'LUN-SAB';
select * from vacunatorios where vacuna_id=1 and foto is not null;
-- ---------------------------------------------------------
INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) 
VALUES		('POSTA JOSE GALVEZ', 14.134421, -32.121, 'AV EL SOL 744', 'LUN-VIE 15:00 - 22:00', null, null);
        
INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) 
VALUES		('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
			('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
			('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
			('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
			('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);
-- ---------------------------------------------------------
select * from vacunatorios where horario_atencion like '%MIE%';
select * from vacunatorios where vacuna_id=1 and foto is not null;
-- ---------------------------------------------------------