def sumar(a,b):
    return a+b



sumar(10,2)
print(sumar(10,5))
print(sumar(a=10,b=5))

parametros={
    'a':10,
    'b':5
}
#destructuracion
#para pasar parametros los valores de un diccionario
print(sumar(**parametros))
print(sumar(**{'a':10,'b':5}))
print(sumar(*[10,5]))

def restar(**kwargs):
    return(kwargs)

print(restar(x=1,y=2,z=3))

def multiplicar(*args):
    return(args)

print(multiplicar(5,4))