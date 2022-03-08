#DFU
#funciones
nombre='Eduardo'

def sumar(numero1,numero2):
    '''funcion que suma dos valores'''
    print('se sumará...')
    print(numero1 + numero2)

sumar(5,7)

def nombre(x):
    '''Muestra documentacion de la funcion si es que hay'''
    print(x)

nombre('Eduardo')
#.doc imprime la documentacion de la funcion
print(nombre.__doc__)


usuario=[]
def registrar(nombre,email,telefono):
    #registramos el usuario 
    usuario.append({
        'nombre': nombre,
        'email': email,
        'telefono': telefono
    })
    return{
        'message':'Usuario registrado exitosamente',
        'usuario':usuario[0]
    },1,True
    #cuando la funcion retorna varios resultados, podemos almacenarlo en una sola variable 
    #o destructuracion de esa tupla en diversas variales
resultado,numero,booleano= registrar ('Eduardo','asdad@gmail.com','3546548')
print(resultado)
print(numero)
print(booleano)
print('--------------------------------------------------------------')
productos=[]
def registrar_productos(nombre,precio,estado=True,almacen='Almacen del cercado'):
    productos.append({
        'nombre':nombre,
        'precio':precio,
        'estado':estado,'almacen':almacen
    })
    return 'producto agregaado exitosamente'

print(registrar_productos('tomates',4.50))
print(registrar_productos('apio',1.40,False))
print(registrar_productos('cebolla',5.30,True,'almacen nuevo mercado'))
print(registrar_productos(almacen='almacen de  la costa',nombre='pescado tilapia',precio=2.50))
print('--------------------------------------------------------------')



#def alumnos(*args):
#   print(args)

print('--------------------------------------------------------------')
#args sirve para enviarle un numero aleatorio de argumentos
def alumnos(clase,*args):    
    if(len(args) and args[0] is not None):
        print('si hay valor del puerto')
    print('la clase es:',clase)
    print('los args son:',args)
alumnos('grupo12','eduardo','nahia','pedro','mario','jean carlo')
alumnos('frntend','eduardo','roxana','luis')
alumnos('juanito')

print('--------------------------------------------------------------')

def ingresarProducto(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('el usuario quiere agregar un producto con el nombre')
    if(kwargs.get('cantidad')):
        print('el usuario quiere ingresar la cantidad del producto')
ingresarProducto(nombre='manzana',precio=2.40,estado=True,pais_procedencia='peru')
ingresarProducto(nombre='pera',precio=1.30,estado=False,pais_procedencia='mexico',cantidad=8)

print('--------------------------------------------------------------')

#recursividad
def saludar_n_veces(limite):
    if(limite==0):
        return ('llegue al limite')
    return saludar_n_veces(limite-1)
resultado=saludar_n_veces(5)

print(resultado)

print('--------------------------------------------------------------')

def factorial(limite):
    if(limite==0):        
        return 1
    return limite*factorial(limite-1)

resultado=factorial(5)
print(resultado)
print('--------------------------------------------------------------')

#operadores termnarios de
nombre_persona = 'Maria'
origen_persona = 'arequipa'

def duda(nombre_persona,origen_persona):
    if nombre_persona == 'Maria' and origen_persona == 'arequipa':
        return 'Me caso'
    else:
        return 'Next'

resultado=duda('Maria','arequipa')
print(resultado)

resultado2='Me caso' if nombre_persona== 'Maria' and origen_persona == 'arequipa' else 'Next'
print(resultado2)

print('--------------------------------------------------------------')

#lambda function

cuadrado=lambda numero: numero ** 2
rpta=cuadrado(4)
print(rpta)
sacar_igv = lambda precio : precio * 0.18
precio_sin_igv=sacar_igv(100)
print(precio_sin_igv)

print('--------------------------------------------------------------')

#global: sirve para utilizar una variable delcarada fuera de la funcion
#una variable local no existe en el global y viceversa

nombre='eduardo'

def saludar():
    #global nombre_persona=nombre*2
    #print(nombre_persona)

#saludar()