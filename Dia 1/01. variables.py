# Instalar Pylance y Python


#TODO: logica para este controlador

#variables de texto
nombre='Joseph'
apellido = "de Mendoza"
descripcion='''hola amigos:
como estan?
yo muy bien jeje'''
desCripcion = "adios"
#print ('hola amigos como estan' , 'a' , 'b' , 'c')

print (descripcion)
print (desCripcion)

#variables numericas
year = 2022
#type() -> mostrara que tipo de variable es
print(type(year))

#Python no se puede crear una variable sin un contenido
#en python None = null undenied
 
especialidad=None
print(type(especialidad))

#en Pyuthon no hace validacion el tipo de datos 
#en Python no existen constantes
dni=[12312313123]
dni='peruano'
dni=False

#id() -> dara la ubicacion en memoria
print(id(dni))

mes,dia= "Febrero",28
print (mes)
#del ->elimina la variable de la memria
del mes
#print(mes)


#concatenar 
print('el nombre es:',nombre,'del usuario')
estado_civil='viudo'
print ('la persona {} es {}'.format(nombre,estado_civil))

print ('{1} es una persona {0}'.format(estado_civil,nombre))
