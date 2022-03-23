from flask_restful import Resource,request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO, PreparacionResponseDTO
from config import conexion

class PreparacionesController(Resource):

    def post(self):
        try:
            body=request.get_json()
            #load: valida diccionaro a parametros definidos en DTO y retorna un diccionario
            data=PreparacionRequestDTO().load(body)
            print(data)
            nuevaPreparacion=Preparacion(**data)
            conexion.session.add(nuevaPreparacion) 
            conexion.session.commit()  
            #dump: convierte instancia a diccionario
            respuesta=PreparacionResponseDTO().dump(nuevaPreparacion)
            return{
                'message':'Preparacion creada exitosamente',
                'preparacion':respuesta
            },201
        except Exception as e:
            conexion.session.rollback()
            return{
                'message':'Error al crear la preparacion',
                'content':e.args
            },400

    def get(self):
        preparacion:Preparacion | None = conexion.session.query(Preparacion).filter_by(id=1).first()
        print(preparacion)
        print(preparacion.orden)
        print(preparacion.receta.nombre)
        print(preparacion.receta_id)
        print(preparacion.receta_id)
        return{
            'message':'ok'
        }


