#if - else
edad=int(input('Edad: '))
if(edad>18):
    #todo lo que escriba adentro pertenece al bloque if
    print('La persona es mayor de edad')
elif (edad>15):
    print('Puedes ingresar a la preparatoria')
else:
    #todo lo escrito aquí es del bloque else es
    print('La persona es menor de edad')
print('finalizo el programa')


datito=int(input('Ingresa un numero: '))
if (datito>500):
    print('No recibe bono yanapai')
elif(datito>=250 and datito<=500):
    print('Recibes el bono ynapai')
else:
    print('Recibes bono ynapai y un balon de gas')
print('finalizo el programa')
