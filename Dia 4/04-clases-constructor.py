class Animal:
    nombre = ''
    sexo=''
    patas=0

    def __init__(self,nombre,sexo,nro_patas):
        self.nombre=nombre
        self.sexo=sexo
        self.patas=nro_patas

    def descripcion(self):
        return 'Yo soy un {1}, soy {2} y tengo {0} patas'.format(self.patas,self.nombre,self.sexo,)
    
foca=Animal('fokita','M',2)
caballo=Animal('caballo','M',4)
gato=Animal('gato','F',4)
print(foca.descripcion())
print(caballo.descripcion())
print(gato.descripcion())