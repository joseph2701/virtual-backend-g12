numero1,numero2 = 10 , 2022

#con el triple igual,
# 
#  compara el contenido y el tipo de dato
print (numero1==numero2)
print (numero1>numero2)
print (numero1>=numero2)
print (numero1<=numero2)
print (numero1<numero2)
print (numero1!=numero2)

#OPERADORES LOGICOS
print ((10 > 5) and (10 < 20))
print ((10 > 5) or (10 < 20))

#OPERADORES DE IDENTIDAD
VERDURAS=['API','LECHUGA','SUCCHINI']
VERDURAS2=VERDURAS
VERDURAS3=['API','LECHUGA','SUCCHINI']
VERDURAS2[0]='PEREJIL'
VERDURAS[1]='MANZANA'
VERDURAS4=VERDURAS.copy()
VERDURAS4[0]='HUACATAY'
print(VERDURAS2 is VERDURAS)
print(VERDURAS)
print(VERDURAS2)
print (VERDURAS3 is VERDURAS)

#si modifias un valor de un primitivo, le cambia la posicion de memoria de la
nombre='eduardo'
nombre2=nombre
print(nombre2 is nombre)
print (id(nombre2))
print (id(nombre))
nombre='fabian'
print (id(nombre2))
print (id(nombre))


#evaluar si es eduardo y nacionalidad peruano o colombiano
nombre='eduardo'
nacionalidad='cubano'
print ((nombre is'eduardo') and (nacionalidad is 'peruano' or nacionalidad is'colombiano'))
print ((nombre =='eduardo') and (nacionalidad == 'peruano' or nacionalidad =='colombiano'))