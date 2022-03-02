#Todo numero no debe comenzar con 0
notas=[10,20,16,8,6,1]
#el for funciona con: lista,tupla,diccionario,conjunto
for nota in notas:
    print(nota)

#imprime bucle manual hasta el limite
for numero in range(10):
    print(numero)

#imprime bucle manual desde valor inicial, hasta el limite
for numero in range(5,10):
    print(numero)

#imprime bucle manual desde valor inicial, hasta el limite segun incremento
for numero in range(5,10,2):
    print(numero)

#imprimir los 3 valores inciales de notas
notas=[10,20,16,8,6,1]

#otra forma
for nota in notas[0:3]:
    print(nota)
#otra forma
print(notas[0:3])
#otra forma
for posicion in range(3):
    print(notas[posicion])