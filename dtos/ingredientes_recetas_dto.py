from config import validador
from models.ingredientes_recetas import IngredientesRecetas
from marshmallow import fields

class IngredientesRecetasRequestDTO(validador.SQLAlchemyAutoSchema):
    
    class Meta:
        model=IngredientesRecetas
        include_fk=True