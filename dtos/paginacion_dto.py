from config import validador
from marshmallow import fields


class PaginacionRequestDTO(validador.Schema):
    #en caso not egna valor la variable, su valor defecto al cargar
    page=fields.Integer(required=False,load_default=1)
    perPage=fields.Integer(required=False,load_default=10)
