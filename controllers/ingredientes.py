from flask_restful import Resource,request
from config import conexion
from models.ingredientes import Ingrediente
#todos los metodos HTTP, se definen como metodos de la clase
class IngredientesController (Resource):
    def get(self):

        #crearemos una sesion para ejecutar query (get)
        resultado=conexion.session.query(Ingrediente).all()
        print(resultado)
        return{
            'message':'Yo soy el get de los ingredientes',
            'content':{
                'id':resultado[0].id,
                'nombre': resultado[0].nombre
            }
        }
    def post(self):
        print(request.get_json())
        try:                
            nuevoIngrediente=Ingrediente()
            nuevoIngrediente.nombre='Leche evaporada'
            #agrega a la db
            conexion.session.add(nuevoIngrediente)
            #guarda cambios en la db de forma permanente
            conexion.session.commit()
        except Exception as e:
            print (e.args)            
            conexion.session.rollback()                
            return{
                'message':'Yo soy el post de los ingredientes',
                'content':e.args[0]
            }

