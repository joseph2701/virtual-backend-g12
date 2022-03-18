from flask_restful import Resource,request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO,RecetaResponseDTO
from config import conexion

##https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
class RecetasController(Resource):
    def post(self):
        body=request.get_json()
        try:
            data=RecetaRequestDTO().load(body)
            #crea la instancia de la nueva receta, pero no la agrega a la db
            nuevaReceta=Receta(
                nombre=data.get('nombre'),
                estado=data.get('estado'),
                comensales=data.get('comensales'),
                duracion=data.get('duracion'),
                dificultad=data.get('dificultad')
            )
            conexion.session.add(nuevaReceta) 
            #al ahcer commit reciens e asigna el id
            conexion.session.commit()
            respuesta=RecetaResponseDTO().dump(nuevaReceta)               
            return{
                'message':'Receta creada exitosamente',
                'content':respuesta
            },201
        except Exception as e:
            return{
                'message':'Error al crear la receta',
                'content':e.args
            }
    def get(self):
        recetas=conexion.session.query(Receta).all()
        respuesta=RecetaResponseDTO(many=True).dump(recetas)
        return{
            'message':'Las recetas son: ',
            'content':respuesta
        }

