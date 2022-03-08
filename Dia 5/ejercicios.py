# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
#print('hola',end='*')
# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()
def dibujar_Rectangulo():
    try:
        print('------------------------------------------')
        print('---------------EJERCICIO 01---------------')
        print('------------------------------------------')
        altura=int(input('Ingresa la altura del rectangulo:'))
        ancho=int(input('Ingresa el ancho del rectangulo:'))
    except Exception as e:    
        print('algo salio mal, intentalo nuevamente')        
        dibujar_Rectangulo()
    else:   
        print('------------------------------------------')
        print('---------------RESULTADO------------------')     
        for y in range(0,altura):
            cad='*'
            for x in range(0,ancho-1):
                cad=cad+'*'
                x+=1            
            print(cad)
            y+=1      
#ejecutamos el primer ejercicio
dibujar_Rectangulo()
print('------------------------------------------')

# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()

def dibujar_Octogono():
    try:
        print('------------------------------------------')
        print('---------------EJERCICIO 02---------------')
        print('------------------------------------------')
        grosor=int(input('Ingresa el grosor del octogono:'))
    except Exception as e:    
        print('algo salio mal, intentalo nuevamente')        
        dibujar_Octogono()
    else:   
        print('------------------------------------------')
        print('---------------RESULTADO------------------')     
        grosor_central=(3 * grosor)-2
        cad='*'
        for inicializa in range(0,grosor-1):
            cad=cad+'*'        
            inicializa+=1
        #pinta la parte de arriba
        for y in range(0,grosor):
            print(cad.center(grosor_central,' '))            
            if (y+1<grosor):
                cad=cad+'**'
            y+=1    
        #pinta la parte central
        for y in range(0,grosor-2):
            print(cad.center(grosor_central,' '))                        
            y+=1
        #pinta la parte inferior        
        for y in range(0,grosor):
            print(cad.center(grosor_central,' '))            
            if (y+1<grosor):
                cad=cad[:-2]
            y+=1           
#ejecutamos el segundo ejercicio
dibujar_Octogono()
print('------------------------------------------')

# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()

def serie_collatz():
    try:
        print('------------------------------------------')
        print('---------------EJERCICIO 03---------------')
        print('------------------------------------------')
        numero=int(input('Ingresa un número:'))
    except Exception as e:    
        print('algo salio mal, intentalo nuevamente')        
        dibujar_Octogono()
    else:   
        print('------------------------------------------')
        print('---------------RESULTADO------------------')     
        print (str(numero),end=' ')
        while numero >1:
            if numero%2==0:
                numero=numero/2                
            else:
                numero=(3*numero)+1
            if(numero>1):
                print (str(int(numero)),end=' ')
            else:
                print (str(int(numero)))
                
#ejecutamos el tercer ejercicio
serie_collatz()
print('------------------------------------------')

# poner a mayuscula la primera letra
print('------------------------------------------')
print('---------------EJERCICIO 04---------------')
print('------------------------------------------')
texto=input('Ingrese el texto a convertir en mayuscula la priemra letra:')
print('---------------RESULTADO------------------')     
texto=texto.title()
print(texto)
print('------------------------------------------')