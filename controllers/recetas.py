from flask_restful import Resource,request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO,RecetaResponseDTO,BuscarRecetaRequestDTO
from dtos.paginacion_dto import PaginacionRequestDTO
from config import conexion
from math import ceil

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
        #agrega la apginacion
        query_params=request.args
        paginacion=PaginacionRequestDTO().load(query_params)
        perPage=paginacion.get('perPage')
        page=paginacion.get('page')        
        skip=perPage*(page-1)

        recetas=conexion.session.query(Receta).limit(perPage).offset(skip).all()
        
        #select count(*) from recetas;
        total=conexion.session.query(Receta).count()
        itemsxPage=perPage if total >=perPage else total
        totalPages=ceil(total/itemsxPage) if itemsxPage>0 else None
        respuesta=RecetaResponseDTO(many=True).dump(recetas)
        return{
            'message':'Las recetas son: ',
            'pagination':{
                'total':total,
                'items':perPage,
                'totalPages':totalPages
            },
            'content':respuesta
        }



class BuscarRecetaController(Resource):

    def get(self):
        query_params=request.args
        try:
            parametros=BuscarRecetaRequestDTO().load(query_params)
            #print(parametros)

            # print(query_params.get('nombre'))
            # nombre_a_buscar=query_params.get('nombre')        
            recetas2=conexion.session.query(Receta).filter(Receta.nombre=='a',Receta.estado==True).all()
            #print(recetas2)

            nombre=parametros.get('nombre','')
            #es lo mismo que si aprametros es not null
            if parametros.get('nombre'):
                del parametros['nombre']

            #haremos la busqueda de todas las resetas 
            #si queremos filtro especifico usamos atributo de la clase
            recetas=conexion.session.query(Receta).filter(Receta.nombre.like('%{}%'.format(nombre))).filter_by(**parametros).all()
            print(recetas)
            resultado=RecetaResponseDTO(many=True).dump(recetas)
            return{
                'message':'',
                'content':resultado
            }
        except Exception as e:
            return{
                'message':'Error a hacer la busqueda',
                'content':e.args
            },400

            #alt + z para saltos de linea continuado