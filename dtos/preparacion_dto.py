from config import validador
from models.preparaciones import Preparacion
from marshmallow import fields
#from dtos.receta_dto import RecetaResponseDTO
from models.recetas import Receta

class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    #validamos que no se acepten espacios vacios
    #nombre=auto_field(validate=validate.And(validate.Length(min=1),validate.Regexp("[A-Z]|[a-z]+")))

    class Meta:
        model=Preparacion
        include_fk=True


class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):    
    class Meta:
        model=Receta

class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    #NESTED: campo que relaciona un DTO con otro DTO,si queremos especificar
    #que atributo queremos jalar, agregamos data_key
    receta=fields.Nested(nested=RecetaResponseDTO,data_key='receta_Relacion')
    class Meta:
        model=Preparacion
        #carga isntancias relacionadas a rpeparacion
        load_instance=True
        include_fk=False
        #agrega al DTO posibls relaciones definidas en orm.relationship
        include_relationships=True