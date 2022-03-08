#dir permite listar los atributros
 #locals () devuelve toda las variables disponiblespython en est scope
print(dir(locals().get('__builtins__')))


#-----------------------------------------------------------
try:
    valor=int(input('Ingresa un numero:'))
    print(valor)
except ValueError:    
    #entra aqui cuando el error es de tipo valueerrorconversion str a int
    print('error al convertir string a numero')
except Exception as e:
    #clausulas permite
    print('algo salio mal, intentalo nuevamente')    
    #cunado tengamos algun error ingresara
    print(e.args)

print('Finaliza correctamente')

print('-----------------------------------------------------------')
while True:
    try:
        valor=int(input('Ingresa un numero: '))
        break
    except:
        print('valor incorrecto, solo pueen ser numeros')
print(valor)

try:
    resultado = 1/1
except:
    print('hubo error')
else:
    #se ejecutara si el funcionamiento fue ok todo
    print ('yo soy el else')
finally:
    #siempre se ejecuta si stuvo bien o error de
    print('yo me ejecutare si todo fue bien y mal')

try:
    #asumiendo que b uscamos producto en la bd y no encontro
    producto=None    
    if(producto is None):
        #raise captura y maneja un error manualmente
        raise Exception('El producto no existe en la bd') 
    
except:
    print('hubo error al encontrar producto')
    #se ejecutara si el funcionamiento fue ok todo    
else:   
    #imprimimos la boleta el ecommerce ya que no huboo errores
    print('boleta impresa')    
finally:
    #siempre se ejecuta si stuvo bien o error de
    print('yo me ejecutare si todo fue bien y mal')

print('-----------------------------------------------------------')

