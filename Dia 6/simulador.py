#factory

from faker import Faker
from faker.providers import internet,phone_number,person
from random import randint,choice

fake = Faker()

#print(fake.name())
#print(fake.ipv4_private())

#se agrega un provider adicional para utilizar los tradicionales
#y de internet
#print('----------------------------------------')

#print(fake.name())
#print(fake.ascii_free_email())

# for i in range(10):
#     print('---------------------------')
#     print('Nombre:      ',fake.first_name())
#     print('Ap. paterno: ',fake.last_name())
#     print('Ap. Materno: ',fake.last_name())
#     print('Email:       ',fake.ascii_email())
#     print('Numero:      ',fake.phone_number())    
#     i+=1

#add_provider necesario cuando sea provider customizado
#fake.add_provider({internet,phone_number,person})
def generar_alumnos(limite):
    for i in range(limite):
        nombre=fake.first_name()
        apePat=fake.last_name()
        apeMat=fake.last_name()
        correo=fake.ascii_email()
        telefono=fake.bothify(text='9########')

        sql='''
        insert into alumnos(nombre,apellido_paterno,apellido_materno,correo,numero_emergencia)
        values ('%s','%s','%s','%s','%s') ;''' % (nombre,apePat,apeMat,correo,telefono)

        # sql2='''
        # insert into alumnos(nombre,apellido_paterno,apellido_materno,correo,numero_emergencia)
        # values ('{}','{}','{}','{}','{}') '''.format (nombre,apePat,apeMat,correo,telefono)
        
        print(sql)   
        i+=1
#generar_alumnos()

def generar_niveles():
    niveles=['Primero','Segundo','Tercero','Cuarto','Quinto','Sexto']
    secciones=['A','B','C']
    ubicaciones=['Sotano','Primer Piso','Segundo Piso','Tercer Piso']
    for nivel in niveles:
        nombre=nivel
        pos_secciones=randint(2,3)        
        # pos_secciones=fake.random_int(min=2,max=3)
        for pos_seccion in range (0,pos_secciones):            
            # pos_ubicacion=fake.random_int(min=0,max=3)
            # ubicacion=ubicaciones[pos_ubicacion]
            ubicacion=choice(ubicaciones)            
            sql='''
            insert into niveles(nombre,seccion,ubicacion)
            values ('%s','%s','%s') ;''' % (nombre,secciones[pos_seccion],ubicacion)
            
            print(sql)   
                
            # print(nombre)
            # print(seccion)
            # print(ubicacion)  

#generar_niveles()


def generar_niveles_alumnos(limite):    
    niveles=['Primero','Segundo','Tercero','Cuarto','Quinto','Sexto']
    secciones=['A','B','C']
    ubicaciones=['Sotano','Primer Piso','Segundo Piso','Tercer Piso']
    for i in range(0,limite):   
        #22 - 121 xq en mi db son el rango de idalumno     
        alumno_id=randint(22,121)
        nivel=niveles[randint(0,5)]
        seccion=secciones[randint(0,2)]        
        print(str(alumno_id) +' - ' + str(nivel) + ' - ' + str(seccion))
                  
        #sql='''
        #insert into niveles(nombre,seccion,ubicacion)
        #values ('%s','%s','%s') ;''' % (nombre,secciones[pos_seccion],ubicacion)
        
        #print(sql)   
            
        # print(nombre)
        # print(seccion)
        # print(ubicacion)  
        i+=1

generar_niveles_alumnos(1)
