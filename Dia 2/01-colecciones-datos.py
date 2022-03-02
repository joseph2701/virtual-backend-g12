#listas

nombre= ['Pedro','Luis','Danny','Cesar','Magaly']
combinada= ['Eduardo',80,False,15.8,[1,2,3]]
#Las listas siempre empiezan en la posicion 0
print(nombre)
#ordena posi: 0 1 2 3 4 izq a derec
print(nombre[4])
#ordena posi: -1 -2 -3 -4 derec a izq
print(nombre[-1])

#pop() -> remueve el ultimo elemento y lo puede almacenar en otro lao
resultado=nombre.pop()
print(resultado)
print(nombre)

#append agrega al final de la listas
nombre.append('Juana')
print(nombre)

#del ->elimina el contenido de una poscion, pero no permite almacenar la lista
del nombre[0]
print(nombre)

#clear -> limpia toda la lista y dejae vacia
nombre.clear()
print(nombre)

#imprimir por posiciones y rangos
#tambien se usa para copiar el contenido
print(combinada)
print(combinada[:])
print(combinada[1:3])
x=combinada[:]
y=combinada
print(id(x))
print(id(combinada))
print(id(y))
print(combinada[:2])
print(combinada[2:])


meses_dscto=['Enero','Marzo','Julio']
mes1='Septiembre'
mes2='Julio'
#in busca el valor y devuelve true
print(mes1 in meses_dscto)
print(mes2 in meses_dscto)
print(mes1 not in meses_dscto)
print(mes2 not in meses_dscto)

seccion_a=['Roxana','Juan']
seccion_b=['Julieta','Martin']
#si hacemos sumatoria se concatenando
print (seccion_a + seccion_b)

#input -> sirve para ingresar datos por el usuario
#dato=input('Ingresa tu nombre: ')
#print('El dato ingresado es: ' + dato)

#TUPLAS
#no se pueden modificar los valores para

cursos=('backend','frontend',1,True)
#cursos[0]='mobile desing' --error
#cursos.append('otra cosa) --error
print(cursos)
print(cursos[0])

#una lista dentro de una tupla si puede ser alterada
variada=(1,2,3,[4,5,6,7,8])
variada[3][0]='Hola'
print (variada)
print(2 in variada)
print(5 in variada)
#creamos una neuva lista apartir de una tupla a partir de una lista
variada_lista=list(variada)
print(variada_lista)
#len -> devuele el num de datos que contiene la
print(len(variada_lista))

#Conjuntos
#coleccion de datos DESORDENADA, una vez creada no se puede ser
# #acceder a las posiciones de sus elementos

estaciones={'Verano','Otonio','Primavera','Invierno'}
print(estaciones)
print('Invierno' in estaciones)
estaciones.add('Otro')
estacion=estaciones.pop()
print(estacion)

#Diccionarios

persona={
    'nombre':'eduardo',
    'apellido':'De Rivero',
    'correo':'edewerw@gmail.com'
}

print(persona)
#realiza la busqueda y en caso de no encontrar devuelve msj
print(persona.get('apellido','No existe'))
#si definimos una llave que no existe, la agrega y sino la actualiza
#NOTA: si la llave n es exactamente igual, creara una nueva
persona['edad']=28
persona['nombre']='Ximena'
print(persona)
#pop -> elimina una llave de un diccionario
persona.pop('apellido')
print(persona)

