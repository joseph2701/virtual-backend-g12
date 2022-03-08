class Usuario:
    def __init__(self,nombre,apellido,correo):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo

    def saludar(self):
        return 'hola soy {}'.format(self.nombre)

class Alumno(Usuario):
    def __init__(self,nombre,apellido,correo,padres):
        #super() llama a la clase de la cual se hace herencias
        super().__init__(nombre,apellido,correo)
        self.padres=padres
        #super() se usa tambien para acceder a los metodos del apdre
    def info(self):
        return{
            'nombre':self.nombre,
            'apellido':self.apellido,
            'padres':self.padres,
            'saludar':super().saludar()
        }

alumnoPedro=Alumno('Pedro','Flores','adfa@gmail.com',[
    {
    'nombre':'wilber',
    'apellido':'Martinez'
    },
    {
    'nombre':'juliana',
    'apellido':'perez'
    },
])

print(alumnoPedro.info())