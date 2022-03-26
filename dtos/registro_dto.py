from config import validador
from marshmallow import validate,fields
from marshmallow_sqlalchemy import auto_field

from models.usuarios import Usuario

class RegistroDTO(validador.SQLAlchemyAutoSchema):       
    correo=auto_field(validate=validate.Email())

    class Meta:
        model=Usuario


class UsuarioResponseDTO(validador.SQLAlchemyAutoSchema):  
    #para que no se muestre la contraseña
    password=auto_field(load_only=True)
    
    class Meta:
        model=Usuario
        
class LoginDTO(validador.Schema):
    correo=fields.Email(required=True)    
    password=fields.String(required=True)
