class Persona:
    def __init__(self,nombre,fec_nac,dni,nacionalidad):
        self.nombre=nombre
        self.fec_nac=fec_nac
        self.nacionalidad=nacionalidad
        self_dni=dni

    def saludar(self):
        print('Hola me llamo {}'.format(self.nombre))
    
class Alumno(Persona):
    def __init__(self,nombre,fec_nac,dni,nacionalidad,cursos):
        super().__init__(nombre,fec_nac,nacionalidad,cursos)
        self.__cursos=cursos

juan=Alumno(nombre='Juan',fec_nac='2000/01/01',dni='01234567',nacionalidad='Peruano',cursos=['Mate','Ciencias'])


