select *
from vacunatorios vc
inner join vacunas v on v.id=vc.vacuna_id;


select *
from vacunatorios vC
LEFT join vacunas v on v.id=vc.vacuna_id;


select * from vacunatorios vC LEFT JOIN Vacunas v on v.id=vc.vacuna_id
UNION
select * from vacunatorios vC RIGHT JOIN Vacunas v on v.id=vc.vacuna_id;

select *
from vacunatorio join vacunas on vacunatorio.vacuna_id=vacunas.id
where nombre='Pfizer';

-- --------------------------------------------------------
select vc.*
from vacunatorios vC
LEFT join vacunas v on v.id=vc.vacuna_id
where v.nombre='SINOPHARM' and vC.horario_atencion='LUN-VIE'  ;
-- --------------------------------------------------------
select v.*
from vacunas v
LEFT join vacunatorios vc on v.id=vc.vacuna_id
where vc.latitud between -5.00 and 10.00;
-- --------------------------------------------------------
select v.*
from vacunas v
LEFT join vacunatorios vc on v.id = vc.vacuna_id
where v.id is null and v.nombre is not null and v.procedencia is not null;

select * from vacunas;
