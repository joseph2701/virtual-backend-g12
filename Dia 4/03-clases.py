#cñases
class Persona:
    fec_nac = '2000-01-01 00:00:00'
    nombre = 'Juan'
    soltero=trueestatura=1.50

    def saludar(self):
        self.decir_nombre()
        self.fec_nac
        print('Hola como estan')
        return 'hola {}'.format(self.nombre)

    def decir_nombre(self):
        print('digo el nombre')


#hay que instanciar
persona1=Persona()
persona2=Persona()
persona2.nombre='Eduardo'
persona1.nombre='Carolina'
persona2.nombre='Josue'
persona2.saludar()
print(persona1.nombre)
#sobreescrive el valor atributo nombre, de toda las instancias que no han sido modificadas
Persona.nombre='Roberto'
print(persona1.nombre)
print(persona2.nombre)
print(Persona.nombre)

