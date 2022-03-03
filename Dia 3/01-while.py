#mienras que

numero=0
# while numero < 10:
#     print ( numero )
#     numero +=1
#     # break
# else:
#     print('EL WHILE TERMINO BIEN')

#SEGUN RELACION DE LOS SIGUIENTES NUMEROS
#indicar  cuantos son pares y cuantos son impares
numeros =[1,5,16,28,234,67,29]
c_par=0
c_impar=0
for numero in numeros:        
    if numero % 2 == 0:
        #print ( 'numero par')        
        c_par+=1
    if numero % 2 != 0:
        #print ( 'numero impar')
        c_impar+=1    
else:
    print(str(c_par) + ' numeros pares')
    print(str(c_impar) + ' numeros impares')

#otra forma
posicion=0
par,impar=0,0
while posicion <len(numeros):
    if numeros[posicion]%2==0:
        par+=1
    else:
        impar+=1
    posicion+=1

print('Hay {} numeros pares'.format(par))
print('Hay {} numeros pares'.format(impar))