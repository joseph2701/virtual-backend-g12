from flask_restful import Resource,request
from config import conexion
from models.ingredientes import Ingrediente
from dtos.dto_prueba import ValidadorPrueba,ValidadorUsuarioPrueba
from marshmallow import validate
from dtos.ingrediente_dto import IngredienteRequestDTO,IngredienteResponseDTO
from marshmallow import ValidationError

#todos los metodos HTTP, se definen como metodos de la clase
class IngredientesController (Resource):
    def get(self):

        #crearemos una sesion para ejecutar query (get)
        resultado=conexion.session.query(Ingrediente).all()
        print(resultado)
        #si queremos serializar la info pero es mas de una sesion
        # colocarle many=True
        ingredientesSerializados=IngredienteResponseDTO(many=True).dump(resultado)
        return{
            'message':'Yo soy el get de los ingredientes',
            'content': ingredientesSerializados
        }
    def post(self):
        print(request.get_json())
        data=request.get_json()
        
        try:                
            data_serializada=IngredienteRequestDTO().load(data)
            print(data_serializada)
            nuevoIngrediente=Ingrediente()
            nuevoIngrediente.nombre=data_serializada.get('nombre')
            #agrega a la db
            conexion.session.add(nuevoIngrediente)
            #guarda cambios en la db de forma permanente
            conexion.session.commit()
            ingredienteSerializado=IngredienteResponseDTO().dump(nuevoIngrediente)
            return{
                'message':'ingrediente creado exitosamente',
                'ingrediente':ingredienteSerializado
            },201

        except ValidationError as e:
            return{
                'message':'La informacion es incorrecta',
                'content':e.args
            },400

        except Exception as e:
            print (e.args)            
            conexion.session.rollback()                
            return{
                'message':'Error alc rear el ingrediente, ya existe',
                'content':e.args[0]
            },500

class PruebaController(Resource):
    def post(self):
        try:                        
            data=request.get_json()        
            validacion=ValidadorPrueba().load(data)
            # validacionLongitud=validate.Length(max=10)
            # validacionLongitud(validacion.get('nombre'))
            print(validacion)
            return{
                'message':'ok',
                'data':validacion
            }
        except Exception as e:
            print(e.args) 
            return{
                'message':'error al recibir los datos',
                'contenido':e.args
            }
    def get(self):
        usuario={
            'nombre':'Eduardo',
            'apellido':'Manrique',
            'nacionalidad':'Peru',
            'password':'mimamamemima'
        }
        resultado=ValidadorUsuarioPrueba().dump(usuario)        
        return{
            'message':'El usuario es: ',
            'content':usuario,
            'resultado':resultado
        }