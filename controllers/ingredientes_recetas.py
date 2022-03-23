from flask_restful import Resource,request
from models.ingredientes_recetas import IngredientesRecetas
from config import conexion
from dtos.ingredientes_recetas_dto import IngredientesRecetasRequestDTO

class IngredientesRecetasControllers(Resource):
    def post(self):
        body=request.get_json()
        try:
            data=IngredientesRecetasRequestDTO().load(body)
            nuevoIR=IngredientesRecetas(**data)

            conexion.session.add(nuevoIR) 
            conexion.session.commit()            

            return{
                'message':'Ingrediente-receta agregado exitosamente'
            },201
        except Exception as e:
            conexion.session.rollback()
            return{
                'message': 'Error al ingresar el ingrediente-receta',
                'content':e.args
            },400