from flask_restful import Resource,request
from models.movimientos import Movimiento
from dtos.movimiento_dto import MovimientoRequestDTO,MovimientoResponseDTO
from flask_jwt import jwt_required,current_identity
from config import conexion

class MovimientoController(Resource):

    @jwt_required()
    def post(self):
        body=request.get_json()
        try:
            print(current_identity)            
            data=MovimientoRequestDTO().load(body)
            data['id_usuario']=current_identity.id
            nuevoMovimiento=Movimiento(**data)
            conexion.session.add(nuevoMovimiento)
            conexion.session.commit()
            resultado=MovimientoResponseDTO().dump(nuevoMovimiento)
            return{
                'message':'Movimiento creado exitosamente',
                'content':resultado
            },201
        except Exception as e:
            return{
                'message':'Error al crear el movimiento',
                'content':e.args
            }        
        
    @jwt_required()
    def get(self):
        #current_identity
         #crearemos una sesion para ejecutar query (get)
        
        #esto se usa para listar en general
        #resultado=conexion.session.query(Movimiento).all()
        #resultadoSerializados=MovimientoResponseDTO(many=True).dump(resultado)
        # return{
        #             'message':'Los movimientos son',
        #             'content': resultadoSerializados
        #         }

        movimientos: list[Movimiento] = conexion.session.query(Movimiento).filter_by(id_usuario=current_identity.id).all()        
        resultado=MovimientoResponseDTO(many=True).dump(movimientos)
        return{
            'message':'Los movimientos son',
            'content': resultado
        }